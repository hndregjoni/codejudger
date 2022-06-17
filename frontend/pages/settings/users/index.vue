
  
<template>
  <v-container fluid fill-height>
    <div class="mx-16 px-11">
      <h1>Manage users </h1>
    </div>
    <v-row class="my-3" style="height: 100%">
      <v-col cols="1"> </v-col>
      <v-col cols="10">
        <v-data-table
          :headers="headers"
          :items="users"
          :items-per-page="5"
          
        ></v-data-table>
      </v-col>

      <v-col cols="auto"> </v-col>
    </v-row>
  </v-container>
</template>




<script>
export default {
  data() {
    return {
      headers: [
         { text: "ID", value: "id" },
        { text: "Username", value: "username" },
        { text: "Email", value: "email" },
        { text: "Full name", value: "fullname" },
       
      ],
      users: [{ username: "", email: "", fullname: "", id: "" }],
    };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    async getUsers() {
      const response = await this.$axios.get("users");

      const data = response.data;
      //   console.log(data);
      this.users = data;
    },
  },
};
</script>

</template>