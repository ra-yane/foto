<template>
  <div class="header">
    <v-toolbar dense flat color="transparent" class="toolbar">
      <div class="display-3">foto.</div>
      <v-spacer></v-spacer>
      <v-btn round
             flat
             large
             color="primary"
             @click.stop="dialog = true"
            >
        <v-icon>add_a_photo</v-icon>&nbsp; Take a picture
      </v-btn>
      <v-dialog v-model="dialog" persistent max-width="600px">
        <v-card>
        <v-card-title>
          <span class="headline">Select your Ingredient</span>
          <v-spacer></v-spacer>
          <v-btn round color="primary" flat icon @click="dialog = false">
            <v-icon>close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12>
                <v-autocomplete
                  :items="['Cheddar', 'Ciabatta', 'Carrot']"
                  label="Ingredient"
                  hint="select an ingredient"
                  required
                ></v-autocomplete>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-autocomplete
                  :items="['Wilkie', 'Igloo', 'Langley']"
                  label="DC"
                  hint="choose the DC where it's been inbounded"
                  required
                ></v-autocomplete>
              </v-flex>
              <v-flex xs12 sm6 md6>
                <v-text-field
                  label="Week"
                  hint="choose the week when it's been inbounded"
                  required
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                {{ pic }}
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <input class="upload"
                 id="photos"
                 type="file"
                 accept="image/*"
                 @change="uploadPictures($event.target.files[0])"
                 multiple>
          <label class="v-btn v-btn--flat v-btn--large v-btn--block v-btn--round theme--light primary--text" for="photos">
            <v-icon color="primary">cloud_upload</v-icon>&nbsp; Upload Pictures
          </label>
        </v-card-actions>
      </v-card>
      </v-dialog>
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
