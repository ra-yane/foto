// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import Vuetify from "vuetify";
import App from "./App";
import router from "./modules/router";
import axios from "axios";

Vue.use(Vuetify, {
  theme: {
    primary: '#BF3636',
    secondary: "#802424",
    error: "#FFCEC6",
    warning: '#ffc852'
  }
});
Vue.config.productionTip = process.env.NODE_ENV === "production";
axios.defaults.withCredentials = true;

new Vue({
  el: "#app",
  router,
  components: {App},
  template: "<App/>"
});
