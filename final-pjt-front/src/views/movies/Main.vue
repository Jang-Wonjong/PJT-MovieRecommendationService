<template>
  <div>
    <div class="movie-detail-image">
      <img src="https://assets.nflxext.com/ffe/siteui/vlv3/03fdc4bf-72f6-4926-83a7-a76e6a1a5591/780e6f4e-6f56-4926-82f5-ee222fb056c0/KR-ko-20211115-popsignuptwoweeks-perspective_alpha_website_medium.jpg" alt="">
    </div>
    <div class="main">
      <div class="text-white">
        <h1>영화, TV 프로그램을 무제한으로.</h1>
        <h2>다양한 디바이스에서 시청하세요. 언제든 해지하실 수 있습니다.</h2>
        <p>{{ this.$store.state }}</p>
        <button @click="moveToLogin" class="btn login-button-color">입장</button>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'Main',
  methods: {
    moveToLogin: function () {
      this.$router.push({
        name: 'Sign'
      })
    },
  },
}
</script>

<style scoped>
.movie-detail-image {
  background-size: cover;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.movie-detail-image::after {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(40, 40, 40);
  opacity: 0.7;
  content: "";
  display: block;
}

.main {
  position: relative;
  z-index: 99;
  margin-top: 100px;
}

.login-button-color {
  color: rgba(245, 245, 245, 0.979);
  background-color: #d63384;
}
</style>