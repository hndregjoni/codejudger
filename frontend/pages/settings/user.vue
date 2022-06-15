<template>
  <v-container >
    <v-row   style="background-color:#FAFAFA; border:solid 1px white;height: 100%">
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-row dense class="my-7 py-3">
          <v-col cols="5" class="d-flex justify-space-around">
            <v-avatar color="primary" size="75">
              <span class="white--text text-h5">HN</span></v-avatar
            >
          </v-col>
          <v-col cols="auto"></v-col>
        </v-row>

        <v-row  dense class="ma-2 ">
          <v-col class="d-flex justify-space-around  pt-2" cols="5">
            <h3>Full name</h3></v-col>
          
          <v-col cols="7" >
            <v-text-field
              v-model="name"
              disabled
              label="Username"
              outlined
              filled="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div style="font-family:'Times New Roman', Times, serif">Username</div></v-col
          >
          <v-col cols="7">
            <v-text-field
              v-model="name"
              disabled
              label="Username"
              outlined
              filled="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Email</h3></div></v-col
          >
          <v-col cols="7">
            <v-text-field
              v-model="name"
              disabled
              label="Username"
              outlined
              filled="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Nationality</h3></div>
          </v-col>
          <v-col cols="7">
            <v-text-field
              v-model="name"
              disabled
              label="Username"
              outlined
              filled="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Occupation</h3></div>
          </v-col>
          <v-col cols="7">
            <v-text-field
              v-model="name"
              disabled
              label="Username"
              outlined
              filled="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Bio</h3></div>
          </v-col>
          <v-col cols="7">
            <v-textarea counter="90"
              outlined solo flat
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Interests</h3></div>
          </v-col>
          <v-col cols="7">
            <v-text-field
              v-model="name"
              disabled
              label="Username"
              outlined
              filled="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="4"> </v-col>
    </v-row>
  </v-container>
</template>
