<template>
  <v-container>
    <v-row
      style="background-color: #fafafa; border: solid 1px white; height: 100%"
    >
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

        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <h3>Full name</h3></v-col
          >

          <v-col cols="7">
            <v-text-field
              v-model="user.name"
              readonly=true
              outlined
              filled
              color="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Username</h3></div></v-col
          >
          <v-col cols="7">
            <v-text-field
              v-model="user.username"
              readonly=true
              outlined
              filled
              color="white"
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
              v-model="user.email"
              readonly="true"
              outlined
              filled
              color="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
        

        <v-row dense class="ma-2">
          <v-col class="d-flex justify-space-around pt-2" cols="5">
            <div><h3>Interests</h3></div>
          </v-col>
          <v-col cols="7">
            <v-text-field
              v-model="user.interest"
              readonly="true"
              
              outlined
              filled
              color="white"
              dense
            ></v-text-field>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="4"> </v-col>
    </v-row>
  </v-container>


  
</template>



<script>
export default {
  data() {
    return {
      user: [{ username: "", email: "", fullname: "", id: "" ,interests:'', }],
    };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    async getUsers() {
       
        try {const response = await this.$axios.get("users/id/2");

      const data = response.data;
      //   console.log(data);
      this.user = data;}
      catch(err){console.log(err);}
      
    },
  },
};
</script>