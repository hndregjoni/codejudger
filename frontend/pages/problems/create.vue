<template>
  <v-container>
    <h1>Create problem</h1>
    <v-row class="my-auto">
      <v-col cols="2">
        <v-text-field
          filled
          outlined
          dense
          v-model="firstname"
          label="Slug"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="8">
        <v-text-field
          filled 
          outlined
          dense
          v-model="firstname"
          label="Title"
          required
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
        filled
        outlined
        name="input-7-4"
        value="Write problem statement here . . ."
      ></v-textarea>
    </v-row>

    <v-row class="ma-auto mb-4">
      Test Cases
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>Test Cases</v-expansion-panel-header>
          <v-expansion-panel-content>
            Here we edit the language constraints
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

    </v-row>


    <v-row class="ma-auto mb-4">
      Constraints
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>Space-Time constraints</v-expansion-panel-header>
          <v-expansion-panel-content>
            Here we edit space and time constraints
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>User constraints</v-expansion-panel-header>
          <v-expansion-panel-content>
            Here we edit user constriants
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>Language constraints</v-expansion-panel-header>
          <v-expansion-panel-content>
            Here we edit the language constraints
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-row>

    <v-row class="ma-auto" justify="center">
      <v-col cols="auto">
        <v-btn block outlined class="primary py-1 px-4"> Create </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>