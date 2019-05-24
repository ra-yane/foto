<template>
  <div class="header">
    Header
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Header',
    data() {
      return {
      }
    },
    methods: {
      logout() {
        auth.logout();
      }
    },
    created() {
      auth.checkAuth().then(() => {
        this.name = auth.user.profile.first_name + " " + auth.user.profile.last_name;
      }).catch((err) => {
        console.log(err);
      });
    }
  };
</script>

<style scoped>
  .header {
    margin: 0.5em;
  }

  @media (min-width: 960px) {
    .header {
      margin: 2em;
    }
  }

  .logo,
  .logo img {
    width: 90%;
    margin-left: 2%;
  }
</style>
