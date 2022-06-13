<template>
  <v-menu
    left
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="this.width/Math.E"
    nudge-bottom="4"
    offset-y
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn fab dense small text v-bind="attrs" v-on="on" size="32">
        <v-icon size="32px">mdi-account-circle</v-icon>
      </v-btn>
    </template>

    <v-card dense flat :width="this.width">
      <v-card-text v-if="this.$auth.loggedIn">
        <v-row justify="center" class="px-7 py-3">
          <v-avatar color="primary" size="80"> PFP </v-avatar>
        </v-row>

        <v-row justify="center">
          {{ this.$auth.loggedIn ? this.$auth.user.username : "" }}
        </v-row>
      </v-card-text>

      <v-card-actions
        v-if="this.$auth.loggedIn"
        style="flex-direction: column"
        justify="center"
      >
        <div style="width: 100%" class="mb-2">
          <v-btn outlined block style="mb-2" color="primary">Profile</v-btn>
        </div>
        <div style="width: 100%">
          <v-btn outlined block color="primary" @click="logout">Logout</v-btn>
        </div>
      </v-card-actions>

      <v-card-actions
        v-if="!this.$auth.loggedIn"
        style="flex-direction: column"
        justify="center"
      >
        <div style="width: 100%">
          <v-btn outlined block color="primary" @click="login">Login</v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </v-menu>
</template>

<script>
export default {
  props: {
    width: {
      type: Number,
      default: 150
    }
  },

  data() {
    return {
        menu: false    
    }
  },

  methods: {
    async login() {
        this.menu = false;
        await this.$router.push("/login");
    },

    async logout() {
      await this.$auth.logout();
      this.menu = false;
      await this.$router.push("/");
    },
  },
};
</script>