<template>
  <v-container style="height: 100%">
    <v-row class="d-flex justify-center mb-5">
      <v-card width="75%">
        <v-card-title> Add Languages </v-card-title>
        <v-row align="center">
          <v-col cols="2"></v-col>
          <v-col cols="4" class="pb-0">
            <v-card-text class="py-0"><h4>Slug :</h4></v-card-text>
            <v-card-actions
              ><v-text-field outlined dense filled></v-text-field
            ></v-card-actions>
          </v-col>
          <!-- <v-col cols="2"></v-col> -->
          <v-col cols="4" class="pb-0">
            <v-card-text class="py-0"><h4>Name :</h4></v-card-text>
            <v-card-actions
              ><v-text-field outlined dense filled></v-text-field>
            </v-card-actions>
          </v-col>
          <v-col class="py-0" cols="2">
            <v-btn class="py-0" tile filled color="#EEEEEE">Add</v-btn></v-col
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
        <v-data-table
          :headers="headers"
          :items="problems"
          :search="search"
        >
        
          <template v-slot:item="row">
          <tr>
            <td>{{row.item.name}}</td>
            <td>{{row.item.slug}}</td>
            <td>{{row.item.created}}</td>
            <td>
                <v-btn color="#EEEEEE"   small >
                    Edit
                </v-btn>
            </td>
          </tr>
      </template>
        
        </v-data-table> </v-card
    ></v-row>
  </v-container>
</template>


<script>
export default {
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Name",
          align: "start",
          // filterable: false,
          value: "name",
        },
        { text: "Slug", value: "slug" },
        { text: "Created", value: "created" },
        { text: "Action", value: "edit" },
      ],
      problems: [
        {
          name: 'sum of products',
          slug: 'abcd',
          created: 'Mon 12 2020',
          edit: '',
        },
        {
         name: 'sum of products',
          slug: 'abcd',
          created: 'Mon 12 2020',
          edit: '',
        },
        {
         name: 'sum of products',
          slug: 'abcd',
          created: 'Mon 12 2020',
          edit: '',
        },
      ],
    };
  },
};
</script>