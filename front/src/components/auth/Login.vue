<template>
  <div class="login">
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <!--<img src="../../assets/logo.png" id="title">-->

        <v-card flat id="card" color="transparent">
          <v-card-title primary-title>
            <div class="text">
              <v-btn block round flat large color="primary" v-on:click="login" id="connect">Log in</v-btn>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Login',
    data() {
      return {
        email: "",
        password: ""
      }
    },
    mounted() {
      let login = this;

      auth.checkAuth().then(() => {
        login.$router.replace('/home');
      }).catch(() => {
      });
    },
    methods: {
      login() {
        auth.login(this);
      }
    }
  }
</script>

<style scoped>
  .login {
    width: 100%;
    text-align: center;
  }

  #title {
    width: 600px;
    max-width: 90%;
    margin-top: 3em;
  }

  #card {
    margin: 4em;
  }

  .text {
    width: 500px;
    max-width: 90%;
    margin: auto;
    text-align: left;
  }

  #connect {
    margin-top: 2em;
    margin-bottom: 2em;
  }
</style>
