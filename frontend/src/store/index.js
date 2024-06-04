export default new Vuex.Store({
  state: {
    dataToSend: null,
  },
  mutations: {
    setUserID(state, payload) {
      state.dataToSend = payload;
    },
  },
  actions: {
    updateUserID({ commit }, payload) {
      commit("setUserID", payload);
    },
  },
});
