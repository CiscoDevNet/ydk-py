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
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

#include <ydk/gnmi_path_api.hpp>
#include <ydk/gnmi_provider.hpp>
#include <ydk/gnmi_service.hpp>
#include <ydk/gnmi_client.hpp>

#include <ydk/logging_callback.hpp>

using namespace pybind11;
using namespace std;

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

static object log_debug;
static object log_info;
static object log_warning;
static object log_error;
static object log_critical;
static bool added_nullhandler = false;
static bool enabled_logging = false;

static void add_null_handler(object logger)
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

void gnmi_debug(const char* msg) { log_debug(msg); }
void gnmi_info(const char* msg) { log_info(msg); }
void gnmi_warning(const char* msg) { log_warning(msg); }
void gnmi_error(const char* msg) { log_error(msg); }
void gnmi_critical(const char* msg) { log_critical(msg); }

static void setup_gnmi_logging()
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

        ydk::set_logging_callback("debug", gnmi_debug);
        ydk::set_logging_callback("info", gnmi_info);
        ydk::set_logging_callback("warning", gnmi_warning);
        ydk::set_logging_callback("error", gnmi_error);
        ydk::set_logging_callback("critical", gnmi_critical);
        enabled_logging = true;

        ydk::set_libyang_logging_callback();
    }
}

PYBIND11_MODULE(ydk_gnmi_, ydk_gnmi)
{
    module providers = ydk_gnmi.def_submodule("providers", "providers module");
    module services  = ydk_gnmi.def_submodule("services", "services module");
    module path      = ydk_gnmi.def_submodule("path", "path module");

    class_<ydk::path::Session>(path, "Session", module_local())
        .def("get_root_schema", &ydk::path::Session::get_root_schema, return_value_policy::reference)
        .def("invoke", (std::shared_ptr<ydk::path::DataNode> (ydk::path::Session::*)(ydk::path::Rpc& rpc) const) &ydk::path::Session::invoke, return_value_policy::reference)
        .def("invoke", (std::shared_ptr<ydk::path::DataNode> (ydk::path::Session::*)(ydk::path::DataNode& rpc) const) &ydk::path::Session::invoke, return_value_policy::reference);

    class_<ydk::path::gNMISession, ydk::path::Session>(path, "gNMISession")
        .def(init<ydk::path::Repository&, const std::string&, int, const std::string&, const std::string&, const std::string&, const std::string&>(),
             arg("repo"),
             arg("address"),
             arg("port"),
             arg("username"),
             arg("password"),
			 arg("server_certificate")="",
			 arg("private_key")="")
        .def("get_root_schema", &ydk::path::gNMISession::get_root_schema, return_value_policy::reference)
        .def("invoke", (std::shared_ptr<ydk::path::DataNode> (ydk::path::gNMISession::*)(ydk::path::Rpc&) const)
             &ydk::path::gNMISession::invoke, arg("rpc"), return_value_policy::reference)
        .def("subscribe", (void (ydk::path::gNMISession::*)
                                 (ydk::path::Rpc& rpc,
                                  std::function<void(const char * response)> out_func,
                                  std::function<bool(const char * response)> poll_func) const)
             &ydk::path::gNMISession::invoke_subscribe,
			                      arg("rpc"),
                                  arg("output_callback_function")=nullptr,
                                  arg("poll_callback_function")=nullptr);

    class_<ydk::ServiceProvider>(providers, "ServiceProvider", module_local())
        .def("get_encoding", &ydk::ServiceProvider::get_encoding, return_value_policy::reference)
        .def("get_session", &ydk::ServiceProvider::get_session, return_value_policy::reference);

    class_<ydk::gNMIServiceProvider, ydk::ServiceProvider>(providers, "gNMIServiceProvider")
        .def(init<ydk::path::Repository&, const string&, int, const string&, const string&, const string&, const string&>(),
            arg("repo"), arg("address"), arg("port"),
			arg("username"), arg("password"),
			arg("server_certificate")="", arg("private_key")="")
        .def("get_encoding", &ydk::gNMIServiceProvider::get_encoding, return_value_policy::reference)
        .def("get_session", &ydk::gNMIServiceProvider::get_session, return_value_policy::reference)
        .def("get_capabilities", &ydk::gNMIServiceProvider::get_capabilities, return_value_policy::reference);

    class_<ydk::gNMISubscription>(services, "gNMISubscription")
        .def(init<>())
        .def_readwrite("entity", &ydk::gNMISubscription::entity)
		.def_readwrite("subscription_mode",  &ydk::gNMISubscription::subscription_mode)
        .def_readwrite("sample_interval", &ydk::gNMISubscription::sample_interval)
        .def_readwrite("suppress_redundant", &ydk::gNMISubscription::suppress_redundant)
        .def_readwrite("heartbeat_interval", &ydk::gNMISubscription::heartbeat_interval);

    class_<ydk::gNMIService>(services, "gNMIService")
	    .def(init<>())
        .def("capabilities", &ydk::gNMIService::capabilities, arg("provider"), return_value_policy::reference)
        .def("get", (shared_ptr<ydk::Entity> (ydk::gNMIService::*)
                (ydk::gNMIServiceProvider & provider, ydk::Entity& filter, const string & operation) const)
                &ydk::gNMIService::get, arg("provider"), arg("filter"), arg ("operation"), return_value_policy::reference)
        .def("get", (vector<shared_ptr<ydk::Entity>> (ydk::gNMIService::*)
                (ydk::gNMIServiceProvider & provider, vector<ydk::Entity*> & filter, const string & operation) const)
                &ydk::gNMIService::get, arg("provider"), arg("filter"), arg ("operation"), return_value_policy::reference)
        .def("set", (bool (ydk::gNMIService::*)(ydk::gNMIServiceProvider & provider, ydk::Entity& entity) const)
                &ydk::gNMIService::set, arg("provider"), arg("entity"), return_value_policy::reference)
        .def("set", (bool (ydk::gNMIService::*)(ydk::gNMIServiceProvider & provider, vector<ydk::Entity*> & entity_list) const)
                &ydk::gNMIService::set, arg("provider"), arg("entity"), return_value_policy::reference)

        .def("subscribe",
                [](ydk::gNMIService& ns,
                   ydk::gNMIServiceProvider& provider,
                   ydk::gNMISubscription& subscription,
                   ydk::uint32 qos = 0,
                   const string & mode = "ONCE",
				   const string & encoding = "PROTO",
                   std::function<void(const char * response)> out_func = nullptr)
                {
                    ns.subscribe(provider, subscription, qos, mode, encoding, out_func);
                })

        .def("subscribe",
                [](ydk::gNMIService& ns,
                   ydk::gNMIServiceProvider& provider,
                   vector<ydk::gNMISubscription*> & subscription_list,
                   ydk::uint32 qos = 0,
                   const string & mode = "ONCE",
				   const string & encoding = "PROTO",
                   std::function<void(const char * response)> out_func = nullptr)
                {
                    ns.subscribe(provider, subscription_list, qos, mode, encoding, out_func);
                });

    setup_gnmi_logging();
};

