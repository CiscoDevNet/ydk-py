"""Craft and import module at  runtime."""

import os
import imp
import sys
import pkgutil
import importlib
from .... import models

__path__ = pkgutil.extend_path(__path__, __name__)


def get_augments_bundles():
    """Collect augmentation contributors."""
    augment_contributors = []
    for (_, name, ispkg) in pkgutil.iter_modules(models.__path__):
        if ispkg:
            try:
                aug_mod = importlib.import_module('ydk.models.%s._aug._meta' % name)
                augment_contributors.append(aug_mod)
            except ImportError:
                continue
    return augment_contributors


def get_pkg_mod_names(path):
    """Return a set for Python module name under path."""
    return {name for _, name, _ in pkgutil.iter_modules(path)}


def patch(base_lines, patch_lines):
    """Add patch to base, patched fields in base are wrapped with @@@."""
    patched_lines = []
    i, j, docstring = 0, 0, False
    while i < len(base_lines) and j < len(patch_lines):
        if base_lines[i] == patch_lines[j]:
            docstring = not docstring if '"""' in base_lines[i] else docstring
            patched_lines.append(base_lines[i])
            i += 1
            j += 1
        elif base_lines[i] == '@@@':
            patched_lines.append('@@@')
            i += 1
            while base_lines[i] != '@@@':
                patched_lines.append(base_lines[i])
                i += 1
            patched_lines.append('@@@')
            i += 1
        else:
            patched_lines.append('@@@')
            idx = j
            if docstring:
                # find next '.. attribute'
                idx += 1
                while ('.. attribute' not in patch_lines[idx]
                       and '"""' not in patch_lines[idx]):
                    idx += 1
                if '"""' in patch_lines[idx]:
                    idx -= 2
            else:
                # code block
                while base_lines[i] != patch_lines[idx]:
                    idx += 1
            while j < idx:
                patched_lines.append(patch_lines[j])
                j += 1
            patched_lines.append('@@@')

    # tail
    if j < len(patch_lines):
        patched_lines.append('@@@')
        while j < len(patch_lines):
            patched_lines.append(patch_lines[j])
            j += 1
        patched_lines.append('@@@')

    return patched_lines


def patch_files(base, paths):
    """Patch files in paths to base."""
    with open(base) as base_file:
        base_lines = base_file.readlines()
        for path in paths:
            with open(path) as patch_file:
                patch_lines = patch_file.readlines()
                try:
                    base_lines = patch(base_lines, patch_lines)
                except IndexError:
                    # inconsistent modules.
                    pass

        return ''.join([l for l in base_lines if l != '@@@'])


def get_patch_paths(path):
    """Return patch module path."""
    base_dir = os.path.dirname(path)
    base_file = os.path.basename(path).rstrip('c')
    patch_mod_path = os.path.join(base_dir, base_file)
    return patch_mod_path


def get_base_module_path(mod_name):
    """Return base module path."""
    base_dir = os.path.dirname(__file__)
    base_mod = os.path.join(base_dir, '%s.py' % mod_name)
    return base_mod


def get_patched_path(mod_name):
    """Return patched module's path."""
    patched_dir = os.path.join(os.path.dirname(__file__), '_aug_patch')
    if not os.path.exists(patched_dir):
        os.makedirs(patched_dir)
    patched_mod = os.path.join(patched_dir, '%s.py' % mod_name)
    return patched_mod


def merge_augmented_modules(mod_name, mod_aug_lst, prefix):
    """Patch augmented module to base module."""
    patch_paths = []
    for mod_fqn in mod_aug_lst:
        mod = importlib.import_module(mod_fqn)
        patch_path = get_patch_paths(mod.__file__)
        patch_paths.append(patch_path)

    base_mod = get_base_module_path(mod_name)
    patched_mod = patch_files(base_mod, patch_paths)
    patched_mod_path = get_patched_path(mod_name)
    with open(patched_mod_path, 'w') as patched_file:
        patched_file.write(patched_mod)

    mod = imp.load_source('.'.join([prefix, mod_name]), patched_mod_path)

    return mod


def shadow_module(augment_contributors):
    """Shadow existing module."""
    to_shadowed = {}

    self_mod_names = get_pkg_mod_names(__path__)

    for module in augment_contributors:
        other_mod_names = get_pkg_mod_names(module.__path__)
        to_update = other_mod_names & self_mod_names

        for mod_name in list(to_update):
            if mod_name != '_meta':
                # we need to patch both meta and API
                mod_fqn = '.'.join([module.__name__, mod_name])
                if mod_name in to_shadowed:
                    to_shadowed[mod_name].append(mod_fqn)
                else:
                    to_shadowed[mod_name] = [mod_fqn]

    for mod_name in to_shadowed:
        mod_aug_lst = to_shadowed[mod_name]
        mod_to_replace = '.'.join([__name__, mod_name])
        mod = merge_augmented_modules(mod_name, mod_aug_lst, __name__)
        sys.modules[mod_to_replace] = mod
        globals()[mod_to_replace] = mod
        # set parent
        parent_mod = sys.modules[__name__]
        setattr(parent_mod, mod_name, mod)


shadow_module(get_augments_bundles())

