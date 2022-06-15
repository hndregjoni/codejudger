<template>
  <v-menu
    left
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="this.width / 2.3"
    nudge-bottom="4"
    offset-y
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn fab dense small text v-bind="attrs" v-on="on" >
        <v-icon > mdi-bell</v-icon>
      </v-btn>
    </template>

    <v-card :width="this.width">
      <v-card-text>
        <v-row justify="center" class="px-7 py-3">
          <v-title><h2>Notifications</h2></v-title>
        </v-row>
      </v-card-text>

      <v-alert
        class="ma-0 mx-1 mb-1 "
        v-for="item in 5"
        :key="item"
        outlined
        dense
        
      >
        <div><h6>Notification {{ item }}</h6> </div>
      </v-alert>
    </v-card>
  </v-menu>
</template>

<script>
export default {
  props: {
    width: {
      type: Number,
      default: 150,
    },
  },

  data() {
    return {
      menu: false,
    };
  },
};
</script>