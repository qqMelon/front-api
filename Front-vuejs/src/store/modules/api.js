const state = {
  user: {
    name: "",
    email: ""
  },
  apiPersistence: {
    status: false,
    token: ""
  }
};

const getters = {
  getUser: state => state.user
};

const actions = {
  callApi: function() {
    // console.log("API caller here !");
    // console.log("API status : ", state.apiPersistence.status);
  }
};

const mutations = {
  setApiPersistence: function(state) {
    state.apiPersistence.status = true;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
