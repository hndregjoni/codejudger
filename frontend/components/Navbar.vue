 <template>
  <v-app-bar app dense elevation="1">
    <v-container>
      <v-row justify="space-between" align="center">
        <v-col>
          <v-menu v-for="link in links" :key="link" offset-y>
            <template v-slot:activator="{ attrs }">
                <v-btn text v-bind="attrs" :to="link.url" class="cj-menu-button" nuxt>
                  {{ link.name }}
                </v-btn>
            </template>
          </v-menu>
        </v-col>

        <v-col cols="auto">
          <span class="logo">
            CodeJudger
          </span>
        </v-col >

        <v-col>
        </v-col>


        <v-col cols="auto">
          <v-avatar justify-end class="mr-10" color="info" size="32"
            >CJ</v-avatar
          >
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
</style>>

<script>
export default {
  data() {
    return {
      links: [
        { name: "Home", url: "/" },
        { name: "Problems", url: "/problems" },
        { name: "Contests", url: "/contests" }
      ],
    };
  },
};
</script>
