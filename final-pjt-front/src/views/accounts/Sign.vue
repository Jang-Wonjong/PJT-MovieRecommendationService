<template>
  <div>
    <div class="movie-detail-image">
      <img src="https://assets.nflxext.com/ffe/siteui/vlv3/03fdc4bf-72f6-4926-83a7-a76e6a1a5591/780e6f4e-6f56-4926-82f5-ee222fb056c0/KR-ko-20211115-popsignuptwoweeks-perspective_alpha_website_medium.jpg" alt="">
    </div>
    <div class="main">
      <div class="row">
        <div class="col-md-6 mx-auto p-0">
          <div class="card">
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
                    <div class="foot"> <label for="tab-1">Already Member?</label> </div>
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
</style>