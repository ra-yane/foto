<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-toolbar color="cyan" dark>
          <v-toolbar-side-icon></v-toolbar-side-icon>

          <v-toolbar-title>Ingredients</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>search</v-icon>
          </v-btn>
        </v-toolbar>

        <v-list two-line>
          <template v-for="ing in ingredients ">
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title v-html="ing.code"></v-list-tile-title>
                <v-list-tile-sub-title v-html="ing.name"></v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        ingredients: undefined,
      }
    },
    mounted() {
      this.getIngredients();
    },
    methods: {
      getIngredients: function () {
        axios.get(process.env.API_URL + '/ingredients').then((response) => {
          if (response.data.msg === "success") {
            this.ingredients = response.data.ingredients;
          }
        })
      },
    }
  }
</script>

<style scoped>
</style>
