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
          
          <v-btn text @click="show=!show">
            <v-icon v-show="show">mdi-white-balance-sunny</v-icon>

            <v-icon v-show="!show">mdi-moon-waxing-crescent</v-icon>

          </v-btn>
          <v-btn text>
            <v-icon>mdi-bell</v-icon>
          </v-btn>

          
          </v-col>
        <v-col cols="auto">
          <div class="text-center">
            <v-menu v-model="menu" :close-on-content-click="false" offset-y>
              <template v-slot:activator="{ on, attrs }">
               
          <v-btn fab dense small text v-bind="attrs"
                  v-on="on"  size="32">
            <v-icon size="32px">mdi-account-circle</v-icon>
          </v-btn>
                
              </template>

              <v-card dense flat>
                <v-list>
                  <v-list-item class="mx-4">
                    <v-list-item-avatar color="primary">
                      IMG
                    </v-list-item-avatar>
                  </v-list-item>

                  <v-list-item>
                    <v-card-title>Username</v-card-title>
                  </v-list-item>
                </v-list>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-list dense class="width=auto">
                    <v-list-item>
                      <v-list-item-action>
                        <v-btn text color="primary">Profile settings</v-btn>
                      </v-list-item-action>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-action>
                        <v-btn text color="primary">Logout</v-btn>
                      </v-list-item-action>
                    </v-list-item>
                  </v-list>
                </v-card-actions>
              </v-card>
            </v-menu>
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
export default {
  data() {
    return {
      show:true,
     
      links: [
        { name: "Home", url: "/" },
        { name: "Problems", url: "/problems" },
        { name: "Contests", url: "/contests" },
      ],
    };
  },
};
</script>
