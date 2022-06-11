<template>
  <v-container fluid class="pa-6">
    <v-card fill-width>
      <v-card-title>
        Problems
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table 
        class="mytab"
        :headers="headers"
        :items="problems"
        :search="search"
      ></v-data-table>
    </v-card>
  </v-container>
</template>

<style>
.mytab th{
   background-color: rgba(74, 72, 199, 0.493);
  
}

</style>

<script>

  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Title',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Difficulty lvl.', value: 'difficulty' },
          { text: 'Date posted', value: 'date' },
          { text: 'Status', value: 'status' },
          { text: 'Tags', value: 'tag' },
        ],
        problems: [
          {
            name: 'Frozen Yogurt',
            difficulty: 159,
            date: 6.0,
            status: 24,
            tag: 4.0,
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%',
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%',
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%',
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%',
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%',
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%',
          },
        ],
      }
    },
  }
</script>