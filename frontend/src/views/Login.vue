<template>
  <div class="login-container d-flex justify-content-center mt-5">
    <div class="login-card mx-4 p-3">
      <form @submit="login">
        <p class="h4 text-center mb-4">Login</p>
        <label for="username-field" class="grey-text">Username</label>
        <input v-model="username" type="text" id="username-field" class="form-control"/>
        <br/>
        <label for="password-field" class="grey-text">Password</label>
        <input type="password" v-model="password" id="password-field" class="form-control"/>
        <div class="text-center mt-4">
          <button class="btn btn-unique" type="submit">Login</button>
        </div>
      </form>
      <b-alert class="mt-2" variant="warning" v-if="loginError" show>Credentials are wrong!</b-alert>
    </div>
  </div>
</template>

<script>
    import {request} from "../request";
    import {appConfig} from "../appConfig";

    export default {
        name: 'Login',
        data: () => {
            return {
                username: '',
                password: '',
                loginError: false
            }
        },
        methods: {
            async login(e) {
                e.preventDefault()
                this.loginError = false
                const {username, password} = this
                try {
                    const res = await request.post(appConfig.TOKEN_AUTH_PATH, {username, password})
                    const {data: {token}} = res
                    localStorage.setItem('token', token);
                    request.defaults.headers['Authorization'] = `Token ${token}`
                    await this.$store.dispatch("setHasAuth", true)
                    this.$router.push('/')
                } catch (e) {
                    console.log("error : ", e)
                    this.loginError = true
                }
            }
        }
    }
</script>

<style>
  
  .login-card {
    width: 400px;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
  }
</style>
