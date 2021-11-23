import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import router from "@/router/index.js";


Vue.use(Vuex)

import axios from 'axios'


export default new Vuex.Store({
  plugins: [
    createPersistedState()  // 새로고침 초기화 방지
  ],
  state: {
    authToken: localStorage.getItem("jwt"),
    id: null,
    username: null,
    nickname: null,
    isLogin: false,
  },
  getters: {
    config: function (state) {
      return {
        Authorization: `JWT ${state.authToken}`,
      };
    },
  },
  mutations: {
    SET_TOKEN: function (state, token) {
      state.authToken = token;
      localStorage.setItem("jwt", token);
      state.isLogin = true
    },
    REMOVE_TOKEN: function (state) {
      localStorage.removeItem("jwt")
      state.authToken = null
      state.isLogin = false
    },
    SAVE_LOGIN_INFO: function (state, data) { // 로그인 정보 저장
      state.id = data.id
      state.username = data.username
      state.nickname = data.nickname
      // state.image = data.image
    },
    UPDATE_PROFILE: function (state, data) {
      state.nickname = data.nickname
      // state.image = data.image
    },
  },
  actions: {
    login: function ({ commit }, credentials) { // 로그인
      axios({
        method: "post",
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: credentials,
      })
        .then((res) => {
          console.log(credentials.username)
          console.log(res)
          commit("SET_TOKEN", res.data.token)
          this.dispatch("loginInfo", credentials.username)
          router.push({ name: "MovieList" })
        })
        .catch(err => {
          console.log(err)
        })
    },
    loginInfo: function ( { commit, getters }, username) { // 로그인 정보 불러오기
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/${username}`,
        headers: getters.config,
      })
      .then((res) => {
        console.log(res)
        const id = res.data.id
        const username = res.data.username
        const nickname = res.data.nickname
        // const image = `${SERVER.URL}` + res.data.image;
        commit("SAVE_LOGIN_INFO", { id, username, nickname})
      })
      .catch(err => {
        console.log(err)
      })
    },
    logout: function ({ commit }) { // 로그아웃
      commit("REMOVE_TOKEN")
      router.push({ name: "Main" })
    },
    signup: function (context, credentials) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: credentials
      })
        .then(() => { // 회원가입 시 자동 로그인
          this.dispatch("login", credentials)
        })
        .catch(err => {
          console.log(err)
        })
    },
    profileUpdate: function ({ commit }, profileItem) {
      const nickname = profileItem.nickname
      // const image = `${SERVER.URL}` + res.data.image
      commit("UPDATE_PROFILE", { nickname });
    },
  },
  modules: {
  }
})
