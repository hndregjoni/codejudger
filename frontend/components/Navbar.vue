 <template>
  <v-app-bar app dense elevation="1">
    <v-container>
      <v-row justify="space-between" align="center">
        <v-col>
          <v-menu v-for="link in links" :key="link" offset-y>
            <template v-slot:activator="{ attrs }">
              <v-btn
                text
                v-bind="attrs"
                :to="link.url"
                class="cj-menu-button"
                nuxt
              >
                {{ link.name }}
              </v-btn>
            </template>
          </v-menu>
        </v-col>

        <v-col cols="auto">
          <span class="logo"> CodeJudger </span>
        </v-col>
        <v-col></v-col>
        <v-col cols="auto">
          <div class="text-center">
            <v-btn fab dense small text @click="toggleMode">
              <v-icon v-show="this.$vuetify.theme.dark"
                >mdi-white-balance-sunny</v-icon
              >

              <v-icon v-show="!this.$vuetify.theme.dark"
                >mdi-moon-waxing-crescent</v-icon
              >
            </v-btn>
            <role-guard>
              <notification-menu :width="250" />
            </role-guard>
            <profile-menu />
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<style lang="scss">
.cj-menu-button {
  border-radius: 20px;
  width: 100px;
  margin-left: 2px;
  margin-right: 2px;
}

.logo {
  font-weight: 700;
  font-size: 18px;
}
</style>

<script>
import NotificationMenu from "./NotificationMenu.vue";
import RoleGuard from "./RoleGuard.vue";
export default {
  components: { NotificationMenu, RoleGuard },
  methods: {
    toggleMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
  },
  data() {
    return {
      menu: false,

      links: [
        { name: "Home", url: "/" },
        { name: "Problems", url: "/problems" },
        { name: "Contests", url: "/contests" },
      ],
    };
  },
};
</script>
