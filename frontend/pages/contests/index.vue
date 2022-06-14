<template>
  <v-container fluid class="pa-6">
    <v-row class="justify-space-around">
      <v-col justify="center">
        <v-card fill-width>
          <v-card-title>
            Problems
            <v-spacer></v-spacer>
            <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line hide-details>
            </v-text-field>
          </v-card-title>
          <v-row>
            <v-select style="width:29%" class="pa-2 ml-3 "
              :items="['Active', 'Finished']" label="Status" v-model="search">
            </v-select>
            <v-select style="width:29%" class="pa-2 mr-3" label="Tags" :items="['Python', 'Java', 'Go', 'Clojure']"
              v-model="search"></v-select>
          </v-row>
          <v-data-table class="mytab" :headers="headers" :items="problems" :search="search" hide-details>
          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="auto">
        <v-card class="pa-2 mb-4">
          <v-btn block outlined text color="black" class="primary" to="/problems/create" nuxt>
            Create problem
          </v-btn>
        </v-card>
        <v-card>

          <v-date-picker v-model="picker"></v-date-picker>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
.mytab th {
  background-color: rgba(74, 72, 199, 0.493);
}
</style>

<script>

export default {
  data() {
    return {
      picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      search: '',

      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Name', value: 'name' ,sortable: false},
        { text: 'Participants', value: 'participants', sortable:false },
        { text: 'Starts', value: 'stars' ,sortable: false },
        { text: 'Ends', value: 'end',sortable: false },
      ],
      problems: [
       
      ],
    }
  },
}
</script>