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
#include <ydk/entity_util.hpp>
#include <ydk/entity_data_node_walker.hpp>
#include <ydk/netconf_service.hpp>
#include <ydk/netconf_provider.hpp>
#include <ydk/opendaylight_provider.hpp>
#include <ydk/restconf_provider.hpp>
#include <ydk/path_api.hpp>
#include <ydk/types.hpp>

#include <spdlog/spdlog.h>
#include <spdlog/sinks/null_sink.h>

#include "Python.h"

using namespace std;
using namespace pybind11;

typedef vector<pair<string, ydk::LeafData>> LeafDataList;
PYBIND11_MAKE_OPAQUE(LeafDataList)

typedef map<std::string, std::shared_ptr<ydk::Entity>> ChildrenMap;
PYBIND11_MAKE_OPAQUE(ChildrenMap)

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

    ydk::EntityPath get_entity_path(ydk::Entity* ancestor) const override {
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

    void set_value(const std::string & value_path, std::string value) override {
        PYBIND11_OVERLOAD_PURE(
            void,
            ydk::Entity,
            set_value,
            value_path,
            value
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

    ChildrenMap & get_children() override {
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
    module types = ydk.def_submodule("types", "types module");
    module path = ydk.def_submodule("path", "path module");
    module entity_utils = ydk.def_submodule("entity_utils", "path module");
    module logging = ydk.def_submodule("logging", "logging");

    bind_vector<LeafDataList>(types, "LeafDataList");

    bind_map<ChildrenMap>(types, "ChildrenMap");

    class_<ydk::path::Capability>(path, "Capability")
        .def(init<const string &, const string &>());

    class_<ydk::path::Annotation>(path, "Annotation")
        .def(init<const string &, const string &, const string &>());

    class_<ydk::path::Statement>(path, "Statement")
        .def(init<const string &, const string &>())
        .def(init<>());

    class_<ydk::path::SchemaNode>(path, "SchemaNode")
        .def("path", &ydk::path::SchemaNode::path, return_value_policy::reference)
        .def("parent", &ydk::path::SchemaNode::parent, return_value_policy::reference)
        .def("root", &ydk::path::SchemaNode::root, return_value_policy::reference)
        .def("statement", &ydk::path::SchemaNode::statement, return_value_policy::reference)
        .def("find", &ydk::path::SchemaNode::find, return_value_policy::reference)
        .def("keys", &ydk::path::SchemaNode::keys, return_value_policy::reference);
//      .def("children", &ydk::path::SchemaNode::children);

    class_<ydk::path::DataNode, shared_ptr<ydk::path::DataNode>>(path, "DataNode")
        .def("schema", &ydk::path::DataNode::schema, return_value_policy::reference)
        .def("path", &ydk::path::DataNode::path, return_value_policy::reference)
        .def("create", (ydk::path::DataNode& (ydk::path::DataNode::*)(const string&)) &ydk::path::DataNode::create, return_value_policy::reference)
        .def("create_filter", (ydk::path::DataNode& (ydk::path::DataNode::*)(const string&)) &ydk::path::DataNode::create_filter, return_value_policy::reference)
        .def("create", (ydk::path::DataNode& (ydk::path::DataNode::*)(const string&, const string&)) &ydk::path::DataNode::create, return_value_policy::reference)
        .def("create_filter", (ydk::path::DataNode& (ydk::path::DataNode::*)(const string&, const string&)) &ydk::path::DataNode::create_filter, return_value_policy::reference)
        .def("get", &ydk::path::DataNode::get, return_value_policy::reference)
        .def("set", &ydk::path::DataNode::set, return_value_policy::reference)
        .def("children", &ydk::path::DataNode::children, return_value_policy::reference)
        .def("root", &ydk::path::DataNode::root, return_value_policy::reference)
        .def("find", &ydk::path::DataNode::find, return_value_policy::reference)
        .def("add_annotation", &ydk::path::DataNode::add_annotation)
        .def("remove_annotation", &ydk::path::DataNode::remove_annotation)
        .def("annotations", &ydk::path::DataNode::annotations, return_value_policy::reference);

    class_<ydk::path::RootSchemaNode, shared_ptr<ydk::path::RootSchemaNode>>(path, "RootSchemaNode")
        .def("path", &ydk::path::RootSchemaNode::path, return_value_policy::reference)
        .def("parent", &ydk::path::RootSchemaNode::parent, return_value_policy::reference)
        .def("find", &ydk::path::RootSchemaNode::find, return_value_policy::reference)
        .def("root", &ydk::path::RootSchemaNode::root, return_value_policy::reference)
//      .def("children", &ydk::path::RootSchemaNode::children)
        .def("statement", &ydk::path::SchemaNode::statement, return_value_policy::reference)
        .def("keys", &ydk::path::SchemaNode::keys, return_value_policy::reference)
        .def("create", (ydk::path::DataNode& (ydk::path::RootSchemaNode::*)(const string&)) &ydk::path::RootSchemaNode::create, return_value_policy::reference)
        .def("create", (ydk::path::DataNode& (ydk::path::RootSchemaNode::*)(const string&, const string&)) &ydk::path::RootSchemaNode::create, return_value_policy::reference)
        .def("rpc", &ydk::path::RootSchemaNode::rpc, return_value_policy::reference);

    class_<ydk::path::ServiceProvider>(path, "ServiceProvider")
        .def("invoke", &ydk::path::ServiceProvider::invoke, return_value_policy::reference)
        .def("get_root_schema", &ydk::path::ServiceProvider::get_root_schema, return_value_policy::reference);

    class_<ydk::path::Rpc, shared_ptr<ydk::path::Rpc>>(path, "Rpc")
        .def("schema", &ydk::path::Rpc::schema, return_value_policy::reference)
        .def("input", &ydk::path::Rpc::input, return_value_policy::reference)
        .def("__call__", &ydk::path::Rpc::operator());

    class_<ydk::path::Repository>(path, "Repository")
        .def(init<>())
        .def(init<const string&>())
        .def("create_root_schema", &ydk::path::Repository::create_root_schema, return_value_policy::move);

    class_<ydk::path::CodecService> codec_service(path, "CodecService");

    codec_service
        .def(init<>())
        .def("encode", &ydk::path::CodecService::encode, return_value_policy::reference)
        .def("decode", &ydk::path::CodecService::decode, return_value_policy::reference);

    enum_<ydk::DataStore>(services, "DataStore")
        .value("candidate", ydk::DataStore::candidate)
        .value("running", ydk::DataStore::running)
        .value("startup", ydk::DataStore::startup)
        .value("url", ydk::DataStore::url);

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

    enum_<ydk::EditOperation>(types, "EditOperation")
        .value("merge", ydk::EditOperation::merge)
        .value("create", ydk::EditOperation::create)
        .value("remove", ydk::EditOperation::remove)
        .value("delete", ydk::EditOperation::delete_)
        .value("replace", ydk::EditOperation::replace)
        .value("not_set", ydk::EditOperation::not_set);

    class_<ydk::Empty>(types, "Empty")
        .def(init<>())
        .def_readwrite("set", &ydk::Empty::set);

    class_<ydk::LeafData>(types, "LeafData")
        .def(init<string, ydk::EditOperation, bool>())
        .def_readonly("value", &ydk::LeafData::value, return_value_policy::reference)
        .def_readonly("operation", &ydk::LeafData::operation, return_value_policy::reference)
        .def_readonly("is_set", &ydk::LeafData::is_set, return_value_policy::reference)
        .def(self == self, return_value_policy::reference);

    class_<ydk::Entity, PyEntity, shared_ptr<ydk::Entity>>(types, "Entity")
        .def(init<>())
        .def("get_entity_path", &ydk::Entity::get_entity_path, return_value_policy::reference)
        .def("get_segment_path", &ydk::Entity::get_segment_path, return_value_policy::reference)
        .def("get_child_by_name", &ydk::Entity::get_child_by_name, return_value_policy::reference)
        .def("set_value", &ydk::Entity::set_value, return_value_policy::reference)
        .def("has_data", &ydk::Entity::has_data, return_value_policy::reference)
        .def("has_operation", &ydk::Entity::has_operation, return_value_policy::reference)
        .def("get_children", &ydk::Entity::get_children, return_value_policy::reference)
        .def("clone_ptr", &ydk::Entity::clone_ptr)
        .def_readwrite("operation", &ydk::Entity::operation)
        .def_readwrite("yang_name", &ydk::Entity::yang_name, return_value_policy::reference)
        .def_readwrite("yang_parent_name", &ydk::Entity::yang_parent_name, return_value_policy::reference)
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
        .def(init<string>())
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
        .def(init<ydk::YType, string>())
        .def("get", &ydk::YLeaf::get, return_value_policy::reference)
        .def("get_name_leafdata", &ydk::YLeaf::get_name_leafdata, return_value_policy::reference)
        .def(self == self, return_value_policy::reference)
        .def("__repr__", &ydk::YLeaf::operator::string, return_value_policy::reference)
        .def("__str__", [](const ydk::YLeaf &yl)
                          {
                               return yl.get();
                          })
        .def("set", (void (ydk::YLeaf::*)(ydk::uint8)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::uint32)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::uint64)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::int8)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::int32)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::int64)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(double)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::Empty)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::Identity)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::Bits)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(std::string)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::Enum::YLeaf)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("set", (void (ydk::YLeaf::*)(ydk::Decimal64)) &ydk::YLeaf::set, return_value_policy::reference)
        .def("[]", &ydk::YLeaf::operator[], return_value_policy::reference)
        .def_readonly("is_set", &ydk::YLeaf::is_set, return_value_policy::reference)
        .def_readwrite("operation", &ydk::YLeaf::operation);

    class_<ydk::YLeafList, PyYLeafList>(types, "YLeafList")
        .def(init<ydk::YType, string>())
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
                            l.getYLeafs().clear();
                        })
        .def_readwrite("operation", &ydk::YLeafList::operation);

    class_<ydk::NetconfServiceProvider>(providers, "NetconfServiceProvider", base<ydk::path::ServiceProvider>())
        .def(init<ydk::path::Repository&, string, string, string, int>())
        .def(init<string, string, string, int>())
        .def("invoke", &ydk::NetconfServiceProvider::invoke, return_value_policy::reference)
        .def("get_root_schema", &ydk::NetconfServiceProvider::get_root_schema, return_value_policy::reference);

    class_<ydk::RestconfServiceProvider>(providers, "RestconfServiceProvider", base<ydk::path::ServiceProvider>())
        .def(init<ydk::path::Repository&, string, string, string, int>())
        .def("invoke", &ydk::RestconfServiceProvider::invoke, return_value_policy::reference)
        .def("get_root_schema", &ydk::RestconfServiceProvider::get_root_schema, return_value_policy::reference);

    class_<ydk::OpenDaylightServiceProvider>(providers, "OpenDaylightServiceProvider")
        .def(init<ydk::path::Repository&, string, string, string, int, ydk::EncodingFormat>())
        .def("get_node_provider", &ydk::OpenDaylightServiceProvider::get_node_provider, return_value_policy::reference)
        .def("get_node_ids", &ydk::OpenDaylightServiceProvider::get_node_ids, return_value_policy::reference);

    class_<ydk::CrudService>(services, "CrudService")
        .def(init<>())
        .def("create", &ydk::CrudService::create, return_value_policy::reference)
        .def("read", &ydk::CrudService::read)
        .def("read_config", &ydk::CrudService::read_config)
        .def("update", &ydk::CrudService::update, return_value_policy::reference)
        .def("delete", &ydk::CrudService::delete_, return_value_policy::reference);

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

    logging.def("EnableLogging", []()
                                 {
                                    Py_Initialize();
                                    // throw away cpp logging records
                                    auto ydk_logger = spdlog::get("ydk");
                                    if (ydk_logger == nullptr)
                                    {
                                        auto null_sink = make_shared<spdlog::sinks::null_sink_st>();
                                        spdlog::details::registry::instance().create("ydk", null_sink);
                                    }
                                 });

    entity_utils.def("get_relative_entity_path", &ydk::get_relative_entity_path);
    entity_utils.def("get_data_node_from_entity", &ydk::get_data_node_from_entity, return_value_policy::reference);
    entity_utils.def("get_entity_from_data_node", &ydk::get_entity_from_data_node);

    ydk.def("is_set", &ydk::is_set);

    return ydk.ptr();
};
