<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-list two-line>
        <v-list-tile
          v-for="ingredient in ingredients"
          :key="ingredient.code"
          avatar
          @click="">
          <v-list-tile-avatar>
            <v-icon>info</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
              {{ ingredient.name }}
            </v-list-tile-title>
            <v-list-tile-sub-title>
              {{ ingredient.code }}
            </v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
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
