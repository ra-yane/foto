<template>
  <div class="header">
    <v-toolbar dense flat color="transparent" class="toolbar">
      <div class="display-3">2Pack</div>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <v-btn icon slot="activator">
          <v-icon>fas fa-ellipsis-v</v-icon>
        </v-btn>
        <v-card>
          <v-list>
            <v-list-tile @click="logout">
              <v-list-tile-title>
                Logout ({{ name }})
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-menu>
    </v-toolbar>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Header',
    data() {
      return {
        name: null,
        user:auth.user.profile,
        dialog: false,
        pic: undefined
      }
    },
    methods: {
      logout() {
        auth.logout();
      },
      uploadPictures(file) {
        let formData = new FormData();
        formData.append('file', file);
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
  .upload {
    width: 0.1px;
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    position: absolute;
    z-index: -1;
  }

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
