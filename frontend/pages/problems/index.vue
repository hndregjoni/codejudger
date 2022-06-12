

<template>
  <v-row justify="center" class="py-7">
    <v-card style="width:55%">
      <v-card-title>
        Problems
        <v-spacer></v-spacer>
        <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line hide-details></v-text-field>
      </v-card-title>
      <v-row>
        <v-select style="width:29%" class="pa-2 ml-3" label="Difficulty level" :items="['easy', 'medium', 'hard']"
          v-model="search"></v-select>
        <v-select style="width:29%" class="pa-2 "
          :items="['Not-attempted', 'Attempted', 'Solved', 'Frozen', 'Disabled']" label="Status" v-model="search">
        </v-select>
        <v-select style="width:29%" class="pa-2 mr-3" label="Tags" :items="['Python', 'Java', 'Go', 'Clojure']"
          v-model="search"></v-select>
      </v-row>
      <v-data-table class="mytab" :headers="headers" :items="filteredItems" :search="search" hide-details>
      </v-data-table>
    </v-card>
  </v-row>
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
      search: '',

      headers: [
        {
          text: 'Title',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Difficulty lvl.', value: 'difficulty' },
        { difficultyLvl: '' },
        { text: 'Date posted', value: 'date', dataType: "Date" },
        { text: 'Status', value: 'status' },
        { text: 'Tags', value: 'tag' },
      ],
      problems: [
        {
          name: 'b',
          difficulty: 'hard',
          date: new Date().toISOString().substring(0, 10),
          status: ' Not-attempted',
          tag: 'Python',
        },
        {
          name: 'a',
          difficulty: 'easy',
          date: new Date().toISOString().substring(0, 10),
          status: 'Attempted',
          tag: 'Java',
        },
        {
          name: 'c',
          difficulty: 'medium',
          date: new Date().toISOString().substring(0, 10),
          status: 'Solved',
          tag: 'Python',
        },
        {
          name: 'e',
          difficulty: ' medium',
          date: new Date().toISOString().substring(0, 10),
          status: 'Attempted',
          tag: 'Java',
        },
        {
          name: 'f',
          difficulty: 'hard',
          date: new Date().toISOString().substring(0, 10),
          status: 'Solved',
          tag: 'Python',
        },
        {
          name: 'd',
          difficulty: 'easy',
          date: new Date().toISOString().substring(0, 10),
          status: 'Solved',
          tag: 'Java',
        },
        {
          name: 'g',
          difficulty: 'hard',
          date: new Date().toISOString().substring(0, 10),
          status: 'Attempted',
          tag: 'Python',
        },
        {
          name: 'j',
          difficulty: 'easy',
          date: new Date().toISOString().substring(0, 10),
          status: 'Frozen',
          tag: 'Go',
        },
        {
          name: 'k',
          difficulty: 'easy',
          date: new Date().toISOString().substring(0, 10),
          status: 'Frozen',
          tag: 'Java',
        },
      ],
    }
  },
  computed: {
    filteredItems() {
      return this.problems.filter((i) => {
        return !this.difficultyLvl || (i.difficulty === this.difficultyLvl);
      })
    }
  }

}
</script>