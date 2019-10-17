import Vue from "vue";
import Vuex from "vuex";

import API from "./modules/api";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    API
  }
});
