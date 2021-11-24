<template>
  <div>
    <div class="movie-detail-image">
      <img src="https://assets.nflxext.com/ffe/siteui/vlv3/03fdc4bf-72f6-4926-83a7-a76e6a1a5591/780e6f4e-6f56-4926-82f5-ee222fb056c0/KR-ko-20211115-popsignuptwoweeks-perspective_alpha_website_medium.jpg" alt="">
    </div>
    <div class="main">
      <div class="row justify-content-center">
        <div class="col-6 mx-auto p-0">
          <div class="card mx-auto">
            <div class="login-box">
              <div class="login-snip"> <input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab">Login</label> <input id="tab-2" type="radio" name="tab" class="sign-up"><label for="tab-2" class="tab">Sign Up</label>
                <div class="login-space">
                  <div class="login">
                    <div class="group">
                      <label for="username" class="label">Username</label>
                      <input id="username" type="text" class="input" placeholder="Enter your username" v-model="login_info.username">
                    </div>
                    <div class="group"> 
                      <label for="password" class="label">Password</label> 
                      <input id="password" type="password" class="input" placeholder="Enter your password" v-model="login_info.password" @keyup.enter="login">
                    </div>
                    <div class="group text-secondary"> <input id="check" type="checkbox" class="check" checked> <label for="check"><span class="icon"></span> Keep me Signed in</label> </div>
                    <div class="group"> 
                      <button class="button" @click="login">SIGN IN</button>
                    </div>
                    <div class="hr"></div>
                    <div class="foot">Forgot Password?</div>
                  </div>
                  <div class="sign-up-form">
                    <div class="group">
                      <label for="username2" class="label">Username</label>
                      <input id="username2" type="text" class="input" placeholder="Create your Username" v-model="singup_info.username">
                    </div>
                    <div class="group">
                      <label for="nickname2" class="label">Nickname</label>
                      <input id="nickname2" type="text" class="input" placeholder="Enter your Nickname" v-model="singup_info.nickname">
                    </div>
                    <div class="group">
                      <label for="password2" class="label">Password</label>
                      <input id="password2" type="password" class="input" placeholder="Create your password" v-model="singup_info.password">
                    </div>
                    <div class="group">
                      <label for="passwordConfirmation" class="label">Repeat Password</label>
                      <input id="passwordConfirmation" type="password" class="input" placeholder="Repeat your password" v-model="singup_info.passwordConfirmation" @keyup.enter="signup">
                    </div>
                    <div class="group">
                      <button class="button" @click="signup">SIGN UP</button>
                    </div>
                    <div class="hr"></div>
                    <!-- <div class="foot"> <label for="tab-1">Already Member?</label> </div> -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'Sign',
  data: function () {
    return {
      login_info: {
        username: null,
        password: null,
      },
      singup_info: {
        username: null,
        nickname: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    login() {
      this.$store.dispatch('login', this.login_info)
    },
    signup() {
      this.$store.dispatch('signup', this.singup_info)
    }
  }
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



/* form */
body {
  margin: 0;
  color: #6a6f8c;
  background: #c8c8c8;
  font: 600 16px/18px 'Open Sans', sans-serif
}

.login-box {
  width: 100%;
  margin: auto;
  max-width: 525px;
  min-height: 670px;
  position: relative;
  background: url(https://assets.nflxext.com/ffe/siteui/vlv3/03fdc4bf-72f6-4926-83a7-a76e6a1a5591/780e6f4e-6f56-4926-82f5-ee222fb056c0/KR-ko-20211115-popsignuptwoweeks-perspective_alpha_website_medium.jpg) no-repeat center;
  box-shadow: 0 12px 15px 0 rgba(0, 0, 0, .24), 0 17px 50px 0 rgba(0, 0, 0, .19)
}

.login-snip {
  width: 100%;
  height: 100%;
  position: absolute;
  padding: 90px 70px 50px 70px;
  background: rgba(44, 44, 44, 0.9)
}

.login-snip .login,
.login-snip .sign-up-form {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  position: absolute;
  transform: rotateY(180deg);
  backface-visibility: hidden;
  transition: all .4s linear
}

.login-snip .sign-in,
.login-snip .sign-up,
.login-space .group .check {
  display: none
}

.login-snip .tab,
.login-space .group .label,
.login-space .group .button {
  text-transform: uppercase
}

.login-snip .tab {
  color: rgba(255, 255, 255, 0.5);
  font-size: 22px;
  margin-right: 15px;
  padding-bottom: 5px;
  margin: 0 15px 10px 0;
  display: inline-block;
  border-bottom: 2px solid transparent
}

.login-snip .sign-in:checked+.tab,
.login-snip .sign-up:checked+.tab {
  color: white;
  border-color: white;
}

.login-space {
  min-height: 345px;
  position: relative;
  perspective: 1000px;
  transform-style: preserve-3d
}

.login-space .group {
  margin-bottom: 15px
}

.login-space .group .label,
.login-space .group .input,
.login-space .group .button {
  width: 100%;
  color: #fff;
  display: block
}

.login-space .group .input,
.login-space .group .button {
  border: none;
  padding: 15px 20px;
  border-radius: 25px;
  background: rgba(255, 255, 255, .1)
}

.login-space .group input[data-type="password"] {
  -webkit-text-security: circle;
}

.login-space .group .label {
  color: #aaa;
  font-size: 12px
}

.login-space .group .button {
  background: #d63384
}

.login-space .group label .icon {
  width: 15px;
  height: 15px;
  border-radius: 2px;
  position: relative;
  display: inline-block;
  background: rgba(255, 255, 255, .1)
}

.login-space .group label .icon:before,
.login-space .group label .icon:after {
  content: '';
  width: 10px;
  height: 2px;
  background: #fff;
  position: absolute;
  transition: all .2s ease-in-out 0s
}

.login-space .group label .icon:before {
  left: 3px;
  width: 5px;
  bottom: 6px;
  transform: scale(0) rotate(0)
}

.login-space .group label .icon:after {
  top: 6px;
  right: 0;
  transform: scale(0) rotate(0)
}

.login-space .group .check:checked+label {
  color: #fff
}

.login-space .group .check:checked+label .icon {
  background: #d63384
}

.login-space .group .check:checked+label .icon:before {
  transform: scale(1) rotate(45deg)
}

.login-space .group .check:checked+label .icon:after {
  transform: scale(1) rotate(-45deg)
}

.login-snip .sign-in:checked+.tab+.sign-up+.tab+.login-space .login {
  transform: rotate(0)
}

.login-snip .sign-up:checked+.tab+.login-space .sign-up-form {
  transform: rotate(0)
}

*,
:after,
:before {
  box-sizing: border-box
}

.clearfix:after,
.clearfix:before {
  content: '';
  display: table
}

.clearfix:after {
  clear: both;
  display: block
}

a {
  color: inherit;
  text-decoration: none
}

.hr {
  height: 2px;
  margin: 60px 0 50px 0;
  background: rgba(255, 255, 255, .2)
}

.foot {
  color: #dddddd;
  text-align: center
}

.card {
  width: 500px;
}

::placeholder {
  color: #b3b3b3
}
</style>