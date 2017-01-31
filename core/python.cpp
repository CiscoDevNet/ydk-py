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

#include <ydk/codec_provider.hpp>
#include <ydk/codec_service.hpp>
#include <ydk/crud_service.hpp>
#include <ydk/entity_util.hpp>
#include <ydk/netconf_provider.hpp>
#include <ydk/opendaylight_provider.hpp>
#include <ydk/restconf_provider.hpp>
#include <ydk/path_api.hpp>
#include <ydk/types.hpp>

using namespace std;
using namespace pybind11;


PYBIND11_PLUGIN(ydk_)
{
	module ydk("ydk_", "YDK module");
	module providers = ydk.def_submodule("providers", "providers module");
	module services = ydk.def_submodule("services", "services module");
	module errors = ydk.def_submodule("errors", "errors module");
	module types = ydk.def_submodule("types", "types module");
	module path = ydk.def_submodule("path", "path module");

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
//		.def("children", &ydk::path::SchemaNode::children);

	class_<ydk::path::DataNode>(path, "DataNode")
		.def("schema", &ydk::path::DataNode::schema, return_value_policy::reference)
		.def("path", &ydk::path::DataNode::path, return_value_policy::reference)
		.def("create", (ydk::path::DataNode* (ydk::path::DataNode::*)(const string&)) &ydk::path::DataNode::create, return_value_policy::reference)
		.def("create_filter", (ydk::path::DataNode* (ydk::path::DataNode::*)(const string&)) &ydk::path::DataNode::create_filter, return_value_policy::reference)
		.def("create", (ydk::path::DataNode* (ydk::path::DataNode::*)(const string&, const string&)) &ydk::path::DataNode::create, return_value_policy::reference)
		.def("create_filter", (ydk::path::DataNode* (ydk::path::DataNode::*)(const string&, const string&)) &ydk::path::DataNode::create_filter, return_value_policy::reference)
		.def("get", &ydk::path::DataNode::get, return_value_policy::reference)
		.def("set", &ydk::path::DataNode::set, return_value_policy::reference)
		.def("children", &ydk::path::DataNode::children, return_value_policy::reference)
		.def("root", &ydk::path::DataNode::root, return_value_policy::reference)
		.def("find", &ydk::path::DataNode::find, return_value_policy::reference)
		.def("add_annotation", &ydk::path::DataNode::add_annotation)
		.def("remove_annotation", &ydk::path::DataNode::remove_annotation)
		.def("annotations", &ydk::path::DataNode::annotations, return_value_policy::reference);

	class_<ydk::path::RootSchemaNode>(path, "RootSchemaNode")
		.def("path", &ydk::path::RootSchemaNode::path, return_value_policy::reference)
		.def("parent", &ydk::path::RootSchemaNode::parent, return_value_policy::reference)
		.def("find", &ydk::path::RootSchemaNode::find, return_value_policy::reference)
		.def("root", &ydk::path::RootSchemaNode::root, return_value_policy::reference)
//		.def("children", &ydk::path::RootSchemaNode::children)
		.def("statement", &ydk::path::SchemaNode::statement, return_value_policy::reference)
		.def("keys", &ydk::path::SchemaNode::keys, return_value_policy::reference)
		.def("create", (ydk::path::DataNode* (ydk::path::RootSchemaNode::*)(const string&) const) &ydk::path::RootSchemaNode::create, return_value_policy::reference)
		.def("create", (ydk::path::DataNode* (ydk::path::RootSchemaNode::*)(const string&, const string&) const) &ydk::path::RootSchemaNode::create, return_value_policy::reference)
		.def("rpc", &ydk::path::RootSchemaNode::rpc, return_value_policy::reference);

	class_<ydk::path::ServiceProvider>(path, "ServiceProvider")
		.def("invoke", &ydk::path::ServiceProvider::invoke, return_value_policy::reference)
		.def("get_root_schema", &ydk::path::ServiceProvider::get_root_schema, return_value_policy::reference);

	class_<ydk::path::Rpc>(path, "Rpc")
		.def("schema", &ydk::path::Rpc::schema, return_value_policy::reference)
		.def("input", &ydk::path::Rpc::input, return_value_policy::reference)
		.def("__call__", &ydk::path::Rpc::operator(), return_value_policy::reference);

	class_<ydk::path::Repository>(path, "Repository")
		.def(init<>())
		.def(init<const string&>())
		.def("create_root_schema", &ydk::path::Repository::create_root_schema, return_value_policy::reference);

	class_<ydk::path::CodecService> codec_service(path, "CodecService");

	codec_service
		.def(init<>())
		.def("encode", &ydk::path::CodecService::encode, return_value_policy::reference)
		.def("decode", &ydk::path::CodecService::decode, return_value_policy::reference);

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
		.value("identityref ", ydk::YType::identityref )
		.value("str", ydk::YType::str)
		.value("boolean", ydk::YType::boolean)
		.value("enumeration", ydk::YType::enumeration)
		.value("bits", ydk::YType::bits)
		.value("decimal64 ", ydk::YType::decimal64);

	enum_<ydk::EditOperation>(types, "EditOperation")
		.value("merge", ydk::EditOperation::merge)
		.value("create", ydk::EditOperation::create)
		.value("remove", ydk::EditOperation::remove)
		.value("delete", ydk::EditOperation::delete_)
		.value("replace", ydk::EditOperation::replace)
		.value("not_set", ydk::EditOperation::not_set)
		;

	class_<ydk::Empty>(types, "Empty")
		.def(init<>())
		.def_readwrite("set", &ydk::Empty::set);

	class_<ydk::LeafData>(types, "LeafData")
		.def(init<string, ydk::EditOperation, bool>())
		.def_readonly("value", &ydk::LeafData::value, return_value_policy::reference)
		.def_readonly("operation", &ydk::LeafData::operation, return_value_policy::reference)
		.def_readonly("is_set", &ydk::LeafData::is_set, return_value_policy::reference)
		.def(self == self, return_value_policy::reference);

	class_<ydk::Entity>(types, "Entity")
		.def("get_entity_path", &ydk::Entity::get_entity_path, return_value_policy::reference)
		.def("get_segment_path", &ydk::Entity::get_segment_path, return_value_policy::reference)
		.def("get_child_by_name", &ydk::Entity::get_child_by_name, return_value_policy::reference)
		.def("set_value", &ydk::Entity::set_value, return_value_policy::reference)
		.def("has_data", &ydk::Entity::has_data, return_value_policy::reference)
		.def("has_operation", &ydk::Entity::has_operation, return_value_policy::reference)
		.def("get_children", &ydk::Entity::get_children, return_value_policy::reference)
		.def("clone_ptr", &ydk::Entity::clone_ptr, return_value_policy::reference)
		.def_readwrite("operation", &ydk::Entity::operation)
		.def_readwrite("yang_name", &ydk::Entity::yang_name, return_value_policy::reference)
		.def_readwrite("yang_parent_name", &ydk::Entity::yang_parent_name, return_value_policy::reference)
		.def_readwrite("parent", &ydk::Entity::parent, return_value_policy::reference);

	class_<ydk::EntityPath>(types, "EntityPath")
		.def(init<string, vector<pair<std::string, ydk::LeafData> > >())
		.def_readonly("path", &ydk::EntityPath::path, return_value_policy::reference)
		.def_readonly("value_paths", &ydk::EntityPath::value_paths, return_value_policy::reference)
		.def(self == self);

	class_<ydk::Bits>(types, "Bits")
		.def(init<>())
		.def("[]", &ydk::Bits::operator[], return_value_policy::reference)
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
		.def_readwrite("value", &ydk::Enum::YLeaf::value)
		.def_readwrite("name", &ydk::Enum::YLeaf::name);

	class_<ydk::YLeaf>(types, "YLeaf")
		.def(init<ydk::YType, string>())
		.def("get", &ydk::YLeaf::get, return_value_policy::reference)
		.def("get_name_leafdata", &ydk::YLeaf::get_name_leafdata, return_value_policy::reference)
		.def(self == self, return_value_policy::reference)
		.def("__repr__", &ydk::YLeaf::operator::string, return_value_policy::reference)
		.def("[]", &ydk::YLeaf::operator[], return_value_policy::reference)
		.def_readonly("is_set", &ydk::YLeaf::is_set, return_value_policy::reference)
		.def_readwrite("operation", &ydk::YLeaf::operation);

	class_<ydk::YLeafList>(types, "YLeafList")
		.def(init<ydk::YType, string>())
		.def("get_name_leafdata", &ydk::YLeafList::get_name_leafdata, return_value_policy::reference)
		.def(self == self, return_value_policy::reference)
		.def("[]", &ydk::YLeafList::operator[], return_value_policy::reference)
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

//	class_<ydk::CodecService>(services, "CodecService")
//		.def(init<>())
//		.def("encode", (string (ydk::CodecService::*)(ydk::CodecServiceProvider &, ydk::Entity &, bool)) &ydk::CodecService::encode, return_value_policy::reference)
//		.def("decode", (std::unique_ptr<ydk::Entity> (ydk::CodecService::*)(ydk::CodecServiceProvider &, string &)) &ydk::CodecService::decode, return_value_policy::reference);

	class_<ydk::YCPPError>(errors, "YPYError")
		.def(init<const string &>())
		.def("what", &ydk::YCPPError::what, return_value_policy::reference)
		.def_readonly("err_msg", &ydk::YCPPError::err_msg);

	class_<ydk::YCPPServiceProviderError>(errors, "YPYServiceProviderError", base<ydk::YCPPError>())
		.def(init<const string &>());

	class_<ydk::YCPPServiceError>(errors, "YPYServiceError", base<ydk::YCPPError>())
		.def(init<const string &>());

	class_<ydk::YCPPInvalidArgumentError>(errors, "YPYInvalidArgumentError", base<ydk::YCPPError>())
		.def(init<const string &>());

	class_<ydk::YCPPOperationNotSupportedError>(errors, "YPYOperationNotSupportedError", base<ydk::YCPPError>())
		.def(init<const string &>());

	class_<ydk::YCPPModelError>(errors, "YPYModelError", base<ydk::YCPPError>())
		.def(init<const string &>());

	ydk.def("get_relative_entity_path", &ydk::get_relative_entity_path);

	ydk.def("is_set", &ydk::is_set);

	return ydk.ptr();
};
