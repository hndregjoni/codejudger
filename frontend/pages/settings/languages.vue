<template>
  <v-container style="height: 100%">
    <v-row class="d-flex justify-center mb-5">
      <v-card width="75%">
        <v-card-title> Add Languages </v-card-title>
        <v-row align="center">
          <v-col cols="4" class="pb-0">
            <v-card-text class="py-0"><h4>ID :</h4></v-card-text>
            <v-card-actions
              ><v-text-field v-model="id" outlined dense filled></v-text-field
            ></v-card-actions>
          </v-col>
          <!-- <v-col cols="2"></v-col> -->
          <v-col cols="4" class="pb-0">
            <v-card-text class="py-0"><h4>Name :</h4></v-card-text>
            <v-card-actions
              ><v-text-field
                v-model="name"
                outlined
                dense
                filled
              ></v-text-field>
            </v-card-actions>
          </v-col>
          <v-col class="py-0" cols="2">
            <v-btn
              class="py-0"
              @click="addLanguages"
              tile
              filled
              color="#EEEEEE"
              >Add</v-btn
            ></v-col
          >
        </v-row>

        <v-row class="ml-2 mb-2" style="width: 90%" clas>
          <v-textarea
            outlined
            counter="100"
            v-model="placeholder"
            filled
            color="white"
            placeholder="write placeholder here . . . ."
          ></v-textarea>
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
        <v-data-table :headers="headers" :items="languages" :search="search">
          <template v-slot:item="row">
            <tr>
              <td>{{ row.item.id }}</td>
              <td>{{ row.item.name }}</td>
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
      id: "",
      name: "",
      placeholder: "",
      headers: [
        {
          text: "ID",
          align: "start",
          value: "id",
        },
        { text: "Name", value: "name" },
        { text: "Action", value: "edit" },
      ],
      languages: [
        {
          id: "",
          name: "",
          edit: "",
        },
      ],
    };
  },
  mounted() {
    this.getLanguages();
  },

  methods: {
    async getLanguages() {
      const response = await this.$axios.get("languages");

      const data = response.data;

      this.languages = data;
    },
    async addLanguages() {
      try {
        const response = await this.$axios.post("languages", {
          id: this.id,
          name: this.name,
          placeholder: this.placeholder,
        });

        this.getLanguages();
        this.id = "";
        this.name = "";
        this.placeholder = "";
      } catch (e) {
        console.log(e);
      }
    },
  },
};
</script>