<template>
  <v-container style="height: 100%">
    <v-row class="d-flex justify-center mb-5">
      <v-card width="75%">
        <v-card-title> Add New </v-card-title>
        <v-row align="center">
          <v-col cols="2"></v-col>
          <v-col cols="4" class="pb-0">
            <v-card-text class="py-0"><h4>Slug :</h4></v-card-text>
            <v-card-actions
              ><v-text-field v-model="slug" outlined dense filled></v-text-field
            ></v-card-actions>
          </v-col>
          <!-- <v-col cols="2"></v-col> -->
          <v-col cols="4" class="pb-0">
            <v-card-text class="py-0"><h4>Name :</h4></v-card-text>
            <v-card-actions
              ><v-text-field
                v-model="title"
                outlined
                dense
                filled
              ></v-text-field>
            </v-card-actions>
          </v-col>
          <v-col class="py-0" cols="2">
            <v-btn class="py-0" tile filled color="#EEEEEE" @click="postTags"
              >Add</v-btn
            ></v-col
          >
        </v-row>
      </v-card>
    </v-row>

    <v-row class="d-flex justify-center mt-5">
      <v-card width="75%">
        <v-card-title>
          <v-col cols="7"> </v-col>
          <v-col cols="5">
            <v-text-field
              v-model="search"
              dense
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-col>
        </v-card-title>
        <v-data-table :headers="headers" :items="tags" :search="search">
          <template v-slot:item="row">
            <tr>
              <td>{{ row.item.id }}</td>
              <td>{{ row.item.name }}</td>
              <td>{{ row.item.slug }}</td>
              <td>{{ row.item.created }}</td>
              <td>
                <v-btn color="#EEEEEE" small> Edit </v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card></v-row
    >
  </v-container>
</template>


<script>
export default {
  data() {
    return {
      search: "",
      slug: "",
      title: "",
      headers: [
        { text: "ID", value: "id" },
        {
          text: "Name",
          align: "start",

          value: "name",
        },
        { text: "Slug", value: "slug" },
        { text: "Created", value: "created" },
        { text: "Action", value: "edit" },
      ],
      tags: [{ id: "", name: "", slug: "", created: "", edit: "" }],
    };
  },

  mounted() {
    this.getTags();
  },

  methods: {
    async getTags() {
      const response = await this.$axios.get("tags");

      const data = response.data;

      this.tags = data;
    },
    async postTags() {
      try {
        const response = await this.$axios.post("tags", {
          slug: this.slug,
          title: this.title,
        });
        this.getTags();
        this.slug='';
        this.title='';

      } catch(e) {console.log("There is an error :(")}
    },
  },
};
</script>