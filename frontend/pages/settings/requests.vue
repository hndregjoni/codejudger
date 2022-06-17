<template>
  <v-container>
    <v-card v-for="i in 5" :key="i">
    <v-row style="border:solid 1px">
    <v-col>
         <v-card-title> Request {{ i }} </v-card-title>
      <v-card-subtitle> </v-card-subtitle>
      <v-card-text> </v-card-text>

    </v-col>
     <v-col>
      <v-card-actions> <v-btn>Approve</v-btn> </v-card-actions></v-col>
     </v-row>
     </v-card>

  </v-container>
</template>