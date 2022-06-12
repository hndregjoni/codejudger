<template>
  <v-container>
    <h1>Create problem</h1>
    <v-row class="my-auto">
      <v-col cols="2">
        <v-text-field
          v-model="firstname"
          label="Slug"
          required
          outlined
          dense
        ></v-text-field>
      </v-col>
      <v-col cols="8">
        <v-text-field
          filled 
          v-model="firstname"
          label="Title"
          required
          outlined
          dense
        ></v-text-field>
      </v-col>

      <v-col cols="2">
         <v-checkbox
         v-model="checkbox"
        label="Slug same as ID"
        dense
         ></v-checkbox>
      </v-col>
    </v-row>

    <v-row class="ma-auto">
      <v-textarea
        outlined
        name="input-7-4"
        value="Write problem statement here . . ."
      ></v-textarea>
    </v-row>
    <v-row class="ma-auto">
      <v-subheader><h2>Languages :</h2> </v-subheader>
      <v-select :items="['Python', 'Java']" placeholder="Language"></v-select>
    </v-row>
    <v-row class="ma-auto">
      <v-expansion-panels inset>
        <v-expansion-panel>
          <v-expansion-panel-header>Constraint</v-expansion-panel-header>
          <v-expansion-panel-content>
            Constraints that will be read from backend
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>

    <v-row class="ma-auto">
      <v-col>
        <v-btn depressed disabled> Upload testcase </v-btn>
      </v-col>
      <v-col>
        <v-btn depressed> Create </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>