<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">ID: </label>
      <input 
        type="text"
        id="username"
        v-model="credentials.username"
      >
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input 
        type="password"
        id="password"
        v-model="credentials.password"
        @keyup.enter="login"
      >
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>


export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login() {
      this.$store.dispatch('login', this.credentials)
    },
  }
}
</script>

<style>

</style>