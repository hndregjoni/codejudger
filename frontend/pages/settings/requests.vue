<template>
  <v-container>
    <v-card   outlined v-for="i in 5" :key="i">
    <v-row style="width=75%" class="my-2" >
    <v-col>
         <v-card-title> User {{ i }} </v-card-title>
      <v-card-subtitle> </v-card-subtitle>
      <v-card-text> </v-card-text>

    </v-col>
     <v-col>
      <v-card-actions> <v-btn >Approve</v-btn> </v-card-actions></v-col>
     </v-row>
     </v-card>

  </v-container>
</template>