import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/auth/Login";
import Callback from "@/components/auth/Callback";
import Main from "@/components/Main";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "login",
      component: Login
    },
    {
      path: "/auth/callback",
      name: "callback",
      component: Callback
    },
    {
      path: "/home",
      name: "home",
      component: Main
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
});
