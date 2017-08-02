/*  ----------------------------------------------------------------
 Copyright 2016 Cisco Systems

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 ------------------------------------------------------------------*/
#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

#include <ydk/codec_provider.hpp>
#include <ydk/codec_service.hpp>
#include <ydk/crud_service.hpp>
#include <ydk/entity_data_node_walker.hpp>
#include <ydk/entity_util.hpp>
#include <ydk/executor_service.hpp>
#include <ydk/filters.hpp>
#include <ydk/logging_callback.hpp>
#include <ydk/netconf_provider.hpp>
#include <ydk/netconf_service.hpp>
#include <ydk/opendaylight_provider.hpp>
#include <ydk/path_api.hpp>
#include <ydk/restconf_provider.hpp>
#include <ydk/types.hpp>
#include <ydk/xml_subtree_codec.hpp>

#include <spdlog/spdlog.h>
#include <spdlog/sinks/null_sink.h>

using namespace pybind11;
using namespace std;

typedef std::vector<std::pair<std::string, ydk::LeafData>> LeafDataList;
PYBIND11_MAKE_OPAQUE(LeafDataList)

typedef std::map<std::string, std::shared_ptr<ydk::Entity>> ChildrenMap;
PYBIND11_MAKE_OPAQUE(ChildrenMap)


static object log_debug;
static object log_info;
static object log_warning;
static object log_error;
static object log_critical;
static bool added_nullhandler = false;
static bool enabled_logging = false;


void add_null_handler(object logger)
{
    if (added_nullhandler) { return; }
    object version = module::import("sys").attr("version_info");
    object ge = version.attr("__ge__");
    // NullHandler is introduced after Python 2.7
    // Add Nullhandler to avoid `handler not found for logger` error for Python > 2.7
    object version_27 = pybind11::make_tuple(2,7);
    bool result = ge(version_27).cast<bool>();
    if (result)
    {
        object null_handler = module::import("logging").attr("NullHandler");
        null_handler = null_handler();
        object add_handler = logger.attr("addHandler");
        add_handler(null_handler);
        added_nullhandler = true;
    }
}

void debug(const char* msg) { log_debug(msg); }
void info(const char* msg) { log_info(msg); }
void warning(const char* msg) { log_warning(msg); }
void error(const char* msg) { log_error(msg); }
void critical(const char* msg) { log_critical(msg); }

void setup_logging()
{
    if (enabled_logging == false)
    {
        object get_logger = module::import("logging").attr("getLogger");
        object logger = get_logger("ydk");

        add_null_handler(logger);
        log_debug = logger.attr("debug");
        log_info = logger.attr("info");
        log_warning = logger.attr("warning");
        log_error = logger.attr("error");
        log_critical = logger.attr("critical");

        ydk::set_logging_callback("debug", debug);
        ydk::set_logging_callback("info", info);
        ydk::set_logging_callback("warning", warning);
        ydk::set_logging_callback("error", error);
        ydk::set_logging_callback("critical", critical);
        enabled_logging = true;
    }
}


using ListCasterBase = detail::list_caster<std::vector<ydk::path::SchemaNode *>, ydk::path::SchemaNode *>;
namespace pybind11{ namespace detail {
template<> struct type_caster<std::vector<ydk::path::SchemaNode *>> : ListCasterBase {
    static handle cast(const std::vector<ydk::path::SchemaNode *> &src, return_value_policy, handle parent) {
        return ListCasterBase::cast(src, return_value_policy::reference, parent);
    }
    static handle cast(const std::vector<ydk::path::SchemaNode *> *src, return_value_policy pol, handle parent) {
        return cast(*src, pol, parent);
    }
};
}}


class PyEntity: public ydk::Entity {
public:

    using ydk::Entity::Entity;

    std::shared_ptr<ydk::Entity> clone_ptr() const override {
        PYBIND11_OVERLOAD(
            std::shared_ptr<ydk::Entity>,
            ydk::Entity,
            clone_ptr,
        );
    }

    const ydk::EntityPath get_entity_path(ydk::Entity* ancestor) const override {
        PYBIND11_OVERLOAD_PURE(
            ydk::EntityPath,
            ydk::Entity,
            get_entity_path,
            ancestor
        );
    }

    std::string get_segment_path() const override {
        PYBIND11_OVERLOAD_PURE(
            std::string,
            ydk::Entity,
            get_segment_path
        );
    }

    bool has_data() const override {
        PYBIND11_OVERLOAD_PURE(
            bool,
            ydk::Entity,
            has_data
        );
    }

    bool has_operation() const override {
        PYBIND11_OVERLOAD_PURE(
            bool,
            ydk::Entity,
            has_operation
        );
    }

    bool has_leaf_or_child_of_name(const std::string & name) const override {
        PYBIND11_OVERLOAD_PURE(
            bool,
            ydk::Entity,
            has_leaf_or_child_of_name,
            name
        );
    }

    void set_value(const std::string & value_path, const std::string & value, const std::string & name_space, const std::string & name_space_prefix) override {
        PYBIND11_OVERLOAD_PURE(
            void,
            ydk::Entity,
            set_value,
            value_path,
            value,
            name_space,
            name_space_prefix
        );
    }

    void set_filter(const std::string & value_path, ydk::YFilter yfilter) override {
        PYBIND11_OVERLOAD_PURE(
            void,
            ydk::Entity,
            set_filter,
            value_path,
            yfilter
        );
    }

    std::shared_ptr<ydk::Entity> get_child_by_name(const std::string & yang_name, const std::string & segment_path="") override {
        PYBIND11_OVERLOAD_PURE(
            std::shared_ptr<ydk::Entity>,
            ydk::Entity,
            get_child_by_name,
            yang_name,
            segment_path
        );
    }

    ChildrenMap get_children() const override {
        PYBIND11_OVERLOAD_PURE(
            ChildrenMap &,
            ydk::Entity,
            get_children,
        );
    }
};

class PyYLeafList : public ydk::YLeafList {
public:
    using ydk::YLeafList::YLeafList;

    void append(ydk::uint8 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::uint32 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::uint64 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::int8 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::int32 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::int64 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(double val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::Empty val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::Identity val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::Bits val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(std::string val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::Enum::YLeaf val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }
    void append(ydk::Decimal64 val) override { PYBIND11_OVERLOAD(void, ydk::YLeafList, append, val); }

    LeafDataList get_name_leafdata() const override {
        PYBIND11_OVERLOAD(
            LeafDataList,
            ydk::YLeafList,
            get_name_leafdata,
        );
    }

    vector<ydk::YLeaf> getYLeafs() const override {
        PYBIND11_OVERLOAD(
            vector<ydk::YLeaf>,
            ydk::YLeafList,
            getYLeafs,
        );
    }

};


PYBIND11_PLUGIN(ydk_)
{
    module ydk("ydk_", "YDK module");
    module providers = ydk.def_submodule("providers", "providers module");
    module services = ydk.def_submodule("services", "services module");
    module filters = ydk.def_submodule("filters", "filters module");
    module types = ydk.def_submodule("types", "types module");
    module path = ydk.def_submodule("path", "path module");
    module entity_utils = ydk.def_submodule("entity_utils", "entity utils module");
    module logging = ydk.def_submodule("logging", "logging");

    bind_vector<LeafDataList>(types, "LeafDataList");

    bind_map<ChildrenMap>(types, "ChildrenMap");

    class_<ydk::path::Capability>(path, "Capability")
        .def(init<const string &, const string &>(),
            arg("model"), arg("revision"));

    class_<ydk::path::Annotation>(path, "Annotation")
        .def(init<const string &, const string &, const string &>(),
            arg("namespace"), arg("name"), arg("value"));

    class_<ydk::path::Statement>(path, "Statement")
        .def(init<const string &, const string &>(), arg("keyword"), arg("arg"))
        .def(init<>())
        .def_readonly("keyword", &ydk::path::Statement::keyword)
        .def_readonly("arg", &ydk::path::Statement::arg);

    class_<ydk::path::SchemaNode, shared_ptr<ydk::path::SchemaNode>>(path, "SchemaNode")
        .def("get_path", &ydk::path::SchemaNode::get_path)
        .def("get_parent", &ydk::path::SchemaNode::get_parent)
        .def("get_root", &ydk::path::SchemaNode::get_root, return_value_policy::reference)
        .def("get_statement", &ydk::path::SchemaNode::get_statement, return_value_policy::reference)
        .def("find", &ydk::path::SchemaNode::find, return_value_policy::reference, arg("path"))
        // .def("get_children", &ydk::path::SchemaNode::get_children)
        .def("get_keys", &ydk::path::SchemaNode::get_keys, return_value_policy::reference);


    class_<ydk::path::DataNode, shared_ptr<ydk::path::DataNode>>(path, "DataNode")
        .def("get_schema_node", &ydk::path::DataNode::get_schema_node, return_value_policy::reference)
        .def("get_path", &ydk::path::DataNode::get_path, return_value_policy::reference)
        .def("create_datanode", (ydk::path::DataNode& (ydk::path::DataNode::*)(const string&)) &ydk::path::DataNode::create_datanode, return_value_policy::reference, arg("path"))
        .def("create_datanode", (ydk::path::DataNode& (ydk::path::DataNode::*)(const string&, const string&)) &ydk::path::DataNode::create_datanode, return_value_policy::reference, arg("path"), arg("value"))
        .def("get_value", &ydk::path::DataNode::get_value, return_value_policy::reference)
        .def("set_value", &ydk::path::DataNode::set_value, return_value_policy::reference, arg("value"))
        .def("get_children", &ydk::path::DataNode::get_children, return_value_policy::reference)
        .def("get_root", &ydk::path::DataNode::get_root, return_value_policy::reference)
        .def("find", &ydk::path::DataNode::find, return_value_policy::reference, arg("path"))
        .def("add_annotation", &ydk::path::DataNode::add_annotation, return_value_policy::reference, arg("annotation"))
        .def("remove_annotation", &ydk::path::DataNode::remove_annotation, return_value_policy::reference, arg("annotation"))
        .def("annotations", &ydk::path::DataNode::annotations, return_value_policy::reference);

    class_<ydk::path::RootSchemaNode, shared_ptr<ydk::path::RootSchemaNode>>(path, "RootSchemaNode")
        .def("get_path", &ydk::path::RootSchemaNode::get_path, return_value_policy::reference)
        .def("get_parent", &ydk::path::RootSchemaNode::get_parent, return_value_policy::reference)
        .def("find", &ydk::path::RootSchemaNode::find, return_value_policy::reference)
        .def("get_root", &ydk::path::RootSchemaNode::get_root, return_value_policy::reference)
//      .def("get_children", &ydk::path::RootSchemaNode::get_children)
        .def("create_datanode", (ydk::path::DataNode& (ydk::path::RootSchemaNode::*)(const string&)) &ydk::path::RootSchemaNode::create_datanode, return_value_policy::reference, arg("path"))
        .def("create_datanode", (ydk::path::DataNode& (ydk::path::RootSchemaNode::*)(const string&, const string&)) &ydk::path::RootSchemaNode::create_datanode, return_value_policy::reference, arg("path"), arg("value"))
        .def("create_rpc", &ydk::path::RootSchemaNode::create_rpc, arg("path"), return_value_policy::reference);

    class_<ydk::path::ServiceProvider>(path, "ServiceProvider")
        .def("invoke", &ydk::path::ServiceProvider::invoke, return_value_policy::reference)
        .def("get_root_schema", &ydk::path::ServiceProvider::get_root_schema, return_value_policy::reference);

    class_<ydk::path::Rpc, shared_ptr<ydk::path::Rpc>>(path, "Rpc")
        .def("get_schema_node", &ydk::path::Rpc::get_schema_node, return_value_policy::reference)
        .def("get_input_node", &ydk::path::Rpc::get_input_node, return_value_policy::reference)
        .def("has_output_node", &ydk::path::Rpc::has_output_node)
        .def("__call__", &ydk::path::Rpc::operator(), arg("service_provider"));

    class_<ydk::path::Repository>(path, "Repository")
        .def(init<>())
        .def(init<ydk::path::ModelCachingOption>())
        .def(init<const string&>())
        .def(init<const string&, ydk::path::ModelCachingOption>())
        .def("create_root_schema",
            (std::shared_ptr<ydk::path::RootSchemaNode> (ydk::path::Repository::*)(const std::vector<ydk::path::Capability>&)) &ydk::path::Repository::create_root_schema,
            return_value_policy::move)
        .def("create_root_schema",
            (std::shared_ptr<ydk::path::RootSchemaNode> (ydk::path::Repository::*)(const std::vector<std::unordered_map<std::string, ydk::path::Capability>>& lookup_tables,
                                                                                   const std::vector<ydk::path::Capability>& caps_to_load))
            &ydk::path::Repository::create_root_schema,
            return_value_policy::move);

    class_<ydk::path::Codec> codec(path, "Codec");

    codec
        .def(init<>())
        .def("encode", &ydk::path::Codec::encode, arg("data_node"), arg("encoding"), arg("pretty"))
        .def("decode", &ydk::path::Codec::decode, arg("root_schema_node"), arg("payload"), arg("encoding"))
        .def("decode_rpc_output", &ydk::path::Codec::decode_rpc_output, arg("root_schema_node"), arg("payload"), arg("rpc_path"), arg("encoding"));

    enum_<ydk::DataStore>(services, "Datastore")
        .value("candidate", ydk::DataStore::candidate)
        .value("running", ydk::DataStore::running)
        .value("startup", ydk::DataStore::startup)
        .value("url", ydk::DataStore::url);

    enum_<ydk::YFilter>(filters, "YFilter")
        .value("merge", ydk::YFilter::merge)
        .value("create", ydk::YFilter::create)
        .value("remove", ydk::YFilter::remove)
        .value("delete", ydk::YFilter::delete_)
        .value("replace", ydk::YFilter::replace)
        .value("read", ydk::YFilter::read)
        .value("not_set", ydk::YFilter::not_set);

    enum_<ydk::EncodingFormat>(types, "EncodingFormat")
        .value("XML", ydk::EncodingFormat::XML)
        .value("JSON", ydk::EncodingFormat::JSON);

    enum_<ydk::YType>(types, "YType")
        .value("uint8", ydk::YType::uint8)
        .value("uint16", ydk::YType::uint16)
        .value("uint32", ydk::YType::uint32)
        .value("uint64", ydk::YType::uint64)
        .value("int8", ydk::YType::int8  )
        .value("int16", ydk::YType::int16 )
        .value("int32", ydk::YType::int32 )
        .value("int64", ydk::YType::int64 )
        .value("empty", ydk::YType::empty )
        .value("identityref", ydk::YType::identityref )
        .value("str", ydk::YType::str)
        .value("boolean", ydk::YType::boolean)
        .value("enumeration", ydk::YType::enumeration)
        .value("bits", ydk::YType::bits)
        .value("decimal64", ydk::YType::decimal64);

    enum_<ydk::path::ModelCachingOption>(types, "ModelCachingOption")
        .value("common", ydk::path::ModelCachingOption::COMMON)
        .value("per_device", ydk::path::ModelCachingOption::PER_DEVICE);

    class_<ydk::Empty>(types, "Empty")
        .def(init<>())
        .def_readwrite("set", &ydk::Empty::set);

    class_<ydk::LeafData>(types, "LeafData")
        .def(init<const string &, ydk::YFilter, bool, const string &, const string &>())
        .def_readonly("value", &ydk::LeafData::value, return_value_policy::reference)
        .def_readonly("yfilter", &ydk::LeafData::yfilter, return_value_policy::reference)
        .def_readonly("is_set", &ydk::LeafData::is_set, return_value_policy::reference)
        .def_readonly("name_space", &ydk::LeafData::name_space, return_value_policy::reference)
        .def_readonly("name_space_prefix", &ydk::LeafData::name_space_prefix, return_value_policy::reference)
        .def(self == self, return_value_policy::reference);

    class_<ydk::Entity, PyEntity, shared_ptr<ydk::Entity>>(types, "Entity")
        .def(init<>())
        .def("get_entity_path", &ydk::Entity::get_entity_path, return_value_policy::reference)
        .def("get_segment_path", &ydk::Entity::get_segment_path, return_value_policy::reference)
        .def("get_child_by_name", &ydk::Entity::get_child_by_name, return_value_policy::reference)
        .def("set_value", &ydk::Entity::set_value, return_value_policy::reference)
        .def("set_filter", &ydk::Entity::set_filter, return_value_policy::reference)
        .def("has_data", &ydk::Entity::has_data, return_value_policy::reference)
        .def("has_operation", &ydk::Entity::has_operation, return_value_policy::reference)
        .def("get_children", &ydk::Entity::get_children, return_value_policy::reference)
        .def("clone_ptr", &ydk::Entity::clone_ptr)
        .def("__eq__", [](ydk::Entity& left, ydk::Entity& right)
                         {
                            return left.operator==(right);
                         })
        .def("__ne__", [](ydk::Entity& left, ydk::Entity& right)
                         {
                            return left.operator!=(right);
                         })
        .def_readwrite("yfilter", &ydk::Entity::yfilter)
        .def_readwrite("yang_name", &ydk::Entity::yang_name, return_value_policy::reference)
        .def_readwrite("yang_parent_name", &ydk::Entity::yang_parent_name, return_value_policy::reference)
        .def_readwrite("is_presence_container", &ydk::Entity::is_presence_container, return_value_policy::reference)
        .def_property("parent", &ydk::Entity::get_parent, &ydk::Entity::set_parent);


    class_<ydk::EntityPath>(types, "EntityPath")
        .def(init<string, vector<pair<std::string, ydk::LeafData> > >())
        .def_readonly("path", &ydk::EntityPath::path, return_value_policy::reference)
        .def_readonly("value_paths", &ydk::EntityPath::value_paths, return_value_policy::reference)
        .def(self == self);

    class_<ydk::Bits>(types, "Bits")
        .def(init<>())
        .def("__getitem__", &ydk::Bits::operator[], return_value_policy::reference)
        .def("__setitem__", []( ydk::Bits &b, std::string key, bool value)
                              {
                                  b[key] = value;
                              })
        .def("get_bitmap", &ydk::Bits::get_bitmap, return_value_policy::reference);

    class_<ydk::Decimal64>(types, "Decimal64")
        .def(init<string>())
        .def_readwrite("value", &ydk::Decimal64::value);

    class_<ydk::Identity>(types, "Identity")
        .def(init<const std::string &, const std::string &, const std::string &>())
        .def("to_string", &ydk::Identity::to_string, return_value_policy::reference);

    class_<ydk::Enum> enum_(types, "Enum");

    enum_.def(init<>());

    class_<ydk::Enum::YLeaf>(enum_, "YLeaf")
        .def(init<int, string>())
        .def("__str__", [](const ydk::Enum::YLeaf &eyl)
                        {
                            return "ydk.types.Enum.YLeaf(" + eyl.name + ")";
                        })
        .def_readwrite("value", &ydk::Enum::YLeaf::value)
        .def_readwrite("name", &ydk::Enum::YLeaf::name);

    class_<ydk::YLeaf>(types, "YLeaf")
        .def(init<ydk::YType, string>(), arg("leaf_type"), arg("name"))
        .def("get", &ydk::YLeaf::get, return_value_policy::reference)
        .def("get_name_leafdata", &ydk::YLeaf::get_name_leafdata, return_value_policy::reference)
        .def(self == self, return_value_policy::reference)
        .def("__repr__", &ydk::YLeaf::operator::string, return_value_policy::reference)
        .def("__str__", [](const ydk::YLeaf &yl)
                          {
                               return yl.get();
                          })
        .def("__getitem__", &ydk::YLeaf::operator[], return_value_policy::reference)
        .def("__setitem__", []( ydk::YLeaf &yl, std::string key, bool value)
                              {
                                  yl[key] = value;
                              })
        .def("set", (void (ydk::YLeaf::*)(ydk::uint8)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::uint32)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::uint64)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::int8)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::int32)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::int64)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(double)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::Empty)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::Identity)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::Bits)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(std::string)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::Enum::YLeaf)) &ydk::YLeaf::set, arg("value"))
        .def("set", (void (ydk::YLeaf::*)(ydk::Decimal64)) &ydk::YLeaf::set, arg("value"))
        .def_readonly("is_set", &ydk::YLeaf::is_set, return_value_policy::reference)
        .def_readwrite("yfilter", &ydk::YLeaf::yfilter)
        .def_readwrite("value_namespace", &ydk::YLeaf::value_namespace)
        .def_readwrite("value_namespace_prefix", &ydk::YLeaf::value_namespace_prefix);

    class_<ydk::YLeafList, PyYLeafList>(types, "YLeafList")
        .def(init<ydk::YType, string>(), arg("leaflist_type"), arg("name"))
        .def("getYLeafs", &ydk::YLeafList::getYLeafs)
        .def("get_name_leafdata", &ydk::YLeafList::get_name_leafdata)
        .def(self == self)
        .def("[]", &ydk::YLeafList::operator[], return_value_policy::reference)
        .def("append", (void (ydk::YLeafList::*)(ydk::uint8)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::uint32)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::uint64)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::int8)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::int32)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::int64)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(double)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::Empty)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::Identity)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::Bits)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(std::string)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::Enum::YLeaf)) &ydk::YLeafList::append)
        .def("append", (void (ydk::YLeafList::*)(ydk::Decimal64)) &ydk::YLeafList::append)
        .def("__getitem__", &ydk::YLeafList::operator[], return_value_policy::reference)
        .def("__len__", []( ydk::YLeafList &l )
                          {
                               return l.getYLeafs().size();
                          })
        .def("clear", []( ydk::YLeafList &l)
                        {
                            l.clear();
                        })
        .def_readwrite("yfilter", &ydk::YLeafList::yfilter);

    class_<ydk::NetconfServiceProvider, ydk::path::ServiceProvider>(providers, "NetconfServiceProvider")
        .def("__init__",
            [](ydk::NetconfServiceProvider &nc_provider, ydk::path::Repository& repo, const string& address, const string& username, const string& password, int port, const string& protocol, bool on_demand) {
                    new(&nc_provider) ydk::NetconfServiceProvider(repo, address, username, password, port, protocol, on_demand);
            },
            arg("repo"),
            arg("address"),
            arg("username"),
            arg("password"),
            arg("port")=830,
            arg("protocol")=string("ssh"),
            arg("on_demand")=true)
        .def("__init__",
            [](ydk::NetconfServiceProvider &nc_provider, const string& address, const string& username, const string& password, int port, const string& protocol, bool on_demand, bool common_cache) {
                    new(&nc_provider) ydk::NetconfServiceProvider(address, username, password, port, protocol, on_demand, common_cache);
            },
            arg("address"),
            arg("username"),
            arg("password"),
            arg("port")=830,
            arg("protocol")=string("ssh"),
            arg("on_demand")=true,
            arg("common_cache")=false)
        .def("__init__",
            [](ydk::NetconfServiceProvider &nc_provider, const string& address, const string& username, const string& password, void* port, const string& protocol, bool on_demand, bool common_cache) {
                    new(&nc_provider) ydk::NetconfServiceProvider(address, username, password, 830, protocol, on_demand, common_cache);
            },
            arg("address"),
            arg("username"),
            arg("password"),
            arg("port")=nullptr,
            arg("protocol")=string("ssh"),
            arg("on_demand")=true,
            arg("common_cache")=false)
        .def("__init__",
            [](ydk::NetconfServiceProvider &nc_provider, const string& address, const string& username, const string& password, int port, bool on_demand, bool common_cache) {
                    new(&nc_provider) ydk::NetconfServiceProvider(address, username, password, port, "ssh", on_demand, common_cache);
            },
            arg("address"),
            arg("username"),
            arg("password"),
            arg("port")=830,
            arg("on_demand")=true,
            arg("common_cache")=false)
        .def("__init__",
            [](ydk::NetconfServiceProvider &nc_provider, const string& address, const string& username, const string& password, bool on_demand, bool common_cache) {
                    new(&nc_provider) ydk::NetconfServiceProvider(address, username, password, 830, "ssh", on_demand, common_cache);
            },
            arg("address"),
            arg("username"),
            arg("password"),
            arg("on_demand")=true,
            arg("common_cache")=false)
        .def("invoke", &ydk::NetconfServiceProvider::invoke, return_value_policy::reference)
        .def("get_root_schema", &ydk::NetconfServiceProvider::get_root_schema, return_value_policy::reference);

    class_<ydk::RestconfServiceProvider, ydk::path::ServiceProvider>(providers, "RestconfServiceProvider")
        .def(init<ydk::path::Repository&, string, string, string, int, ydk::EncodingFormat>(),
            arg("repo"), arg("address"), arg("username"), arg("password"), arg("port"), arg("encoding"))
        .def("invoke", &ydk::RestconfServiceProvider::invoke, return_value_policy::reference)
        .def("get_root_schema", &ydk::RestconfServiceProvider::get_root_schema, return_value_policy::reference);

    class_<ydk::OpenDaylightServiceProvider>(providers, "OpenDaylightServiceProvider")
        .def(init<ydk::path::Repository&, string, string, string, int, ydk::EncodingFormat>(),
            arg("repo"), arg("address"), arg("username"), arg("password"), arg("port"), arg("encoding"))
        .def("get_node_provider", &ydk::OpenDaylightServiceProvider::get_node_provider, return_value_policy::reference)
        .def("get_node_ids", &ydk::OpenDaylightServiceProvider::get_node_ids, return_value_policy::reference);

    class_<ydk::CrudService>(services, "CRUDService")
        .def(init<>())
        .def("create", &ydk::CrudService::create, return_value_policy::reference)
        .def("read", &ydk::CrudService::read)
        .def("read_config", &ydk::CrudService::read_config)
        .def("update", &ydk::CrudService::update, return_value_policy::reference)
        .def("delete", &ydk::CrudService::delete_, return_value_policy::reference);

    class_<ydk::ExecutorService>(services, "ExecutorService")
        .def(init<>())
        .def("execute_rpc", &ydk::ExecutorService::execute_rpc, arg("provider"), arg("entity"),
            arg("top_entity") = nullptr);

    class_<ydk::NetconfService>(services, "NetconfService")
        .def(init<>())
        .def("cancel_commit", &ydk::NetconfService::cancel_commit,
            arg("provider"), arg("persist-id") = -1,
            return_value_policy::reference)
        .def("close_session", &ydk::NetconfService::close_session,
            arg("provider"))
        .def("commit", &ydk::NetconfService::commit,
            arg("provider"), arg("confirmed") = false,
            arg("confirm_timeout") = -1, arg("persist") = -1,
            arg("persist-id") = -1, return_value_policy::reference)
        .def("copy_config", (bool (ydk::NetconfService::*)(ydk::NetconfServiceProvider&,
            ydk::DataStore,
            ydk::DataStore,
            std::string)) &ydk::NetconfService::copy_config,
            arg("provider"),
            arg("target"),
            arg("source"),
            arg("url") = std::string{""},
            return_value_policy::reference)
        .def("copy_config", (bool (ydk::NetconfService::*)(ydk::NetconfServiceProvider&,
            ydk::DataStore,
            ydk::Entity&)) &ydk::NetconfService::copy_config,
            arg("provider"),
            arg("target"),
            arg("source_config"),
            return_value_policy::reference)
        .def("delete_config", &ydk::NetconfService::delete_config,
            arg("provider"), arg("target"), arg("url") = std::string{""},
            return_value_policy::reference)
        .def("discard_changes", &ydk::NetconfService::discard_changes,
            arg("provider"), return_value_policy::reference)
        .def("edit_config", &ydk::NetconfService::edit_config,
            arg("provider"), arg("target"), arg("config"),
            arg("default_operation") = std::string{""}, arg("test_option") = std::string{""},
            arg("error_option") = std::string{""}, return_value_policy::reference)
        .def("get_config", &ydk::NetconfService::get_config,
            arg("provider"), arg("source"), arg("filter"))
        .def("get", &ydk::NetconfService::get,
            arg("provider"), arg("filter"), return_value_policy::reference)
        .def("kill_session", &ydk::NetconfService::kill_session,
            arg("provider"), arg("session_id"), return_value_policy::reference)
        .def("lock", &ydk::NetconfService::lock,
            arg("provider"), arg("target"), return_value_policy::reference)
        .def("unlock", &ydk::NetconfService::unlock,
            arg("provider"), arg("target"), return_value_policy::reference)
        .def("validate",
            (bool (ydk::NetconfService::*)(ydk::NetconfServiceProvider&,
            ydk::DataStore,
            std::string)) &ydk::NetconfService::validate,
            "doc",
            arg("provider"),
            arg("source"),
            arg("url") = std::string{""},
            return_value_policy::reference)
        .def("validate",
            (bool (ydk::NetconfService::*)(ydk::NetconfServiceProvider&,
            ydk::Entity&)) &ydk::NetconfService::validate,
            arg("provider"),
            arg("source_config"),
            return_value_policy::reference);

    class_<ydk::XmlSubtreeCodec>(entity_utils, "XmlSubtreeCodec")
        .def(init<>())
        .def("encode", &ydk::XmlSubtreeCodec::encode, return_value_policy::reference)
        .def("decode", &ydk::XmlSubtreeCodec::decode);

    entity_utils.def("get_relative_entity_path", &ydk::get_relative_entity_path);
    entity_utils.def("get_entity_from_data_node", &ydk::get_entity_from_data_node);
    #if defined(PYBIND11_OVERLOAD_CAST)
    entity_utils.def("get_data_node_from_entity", overload_cast<ydk::Entity&, ydk::path::RootSchemaNode&>(&ydk::get_data_node_from_entity), return_value_policy::reference);
    #else
    entity_utils.def("get_data_node_from_entity", static_cast<ydk::path::DataNode& (*)(ydk::Entity&, ydk::path::RootSchemaNode&)>(&ydk::get_data_node_from_entity), return_value_policy::reference);
    #endif

    ydk.def("is_set", &ydk::is_set);

    setup_logging();

    return ydk.ptr();
};
