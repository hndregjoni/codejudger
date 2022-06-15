<template>
  <!-- <div v-if="value1" > -->
  <v-content v-if="value1" fill-height fluid>
    <v-row justify="center" class="py-10">
      <v-row justify="center" class="pt-5">
        <v-btn class="mx-2" outlined fab color="black">
          <v-icon>mdi-github</v-icon>
        </v-btn>
        <v-btn class="mx-2" outlined fab color="red">
          <v-icon>mdi-google</v-icon>
        </v-btn>
        <v-btn class="mx-2" outlined fab color="blue">
          <v-icon>mdi-facebook</v-icon>
        </v-btn>
      </v-row>
    </v-row>
    <v-row justify="center">
      <h3>or</h3>
    </v-row>
    <v-row justify="center">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="name"
          :counter="10"
          :rules="nameRules"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :type="'email'"
          label="Email"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :type="'password'"
          :rules="passwordRules"
          label="Password"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :type="'password'"
          :rules="passwordRules"
          label="Confirm password"
          required
        ></v-text-field>

        <v-row class="mt-5"> </v-row>
        <v-row>
          <v-btn
            @click="(value1 = false), (value2 = true)"
            block
            class="btn"
            outlined
            text
            color="black"
          >
            Next
          </v-btn>
        </v-row>
      </v-form>
    </v-row>
  </v-content>

  <v-content v-else-if="value2" class="pb-10">
    <v-row justify="center">
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          v-model="name"
          :rules="nameRules"
          label="Full name"
          required
        ></v-text-field>

        <v-select
          placeholder="0"
          class="gender pa-0"
          v-model="gender"
          :items="['Male', 'Female', 'Non-binary']"
          label="Gender"
          required
        ></v-select>

        <v-label>Bio</v-label>

        <v-textarea counter="90" solo></v-textarea>

        <v-combobox
          v-model="chips"
          :items="['Python', 'Java', 'Go', 'Clojure', 'DFS', 'BFS']"
          chips
          clearable
          label="Interests"
          multiple
          prepend-icon="mdi-filter-variant"
          solo
        >
          <template v-slot:selection="{ attrs, item, select, selected }">
            <v-chip
              v-bind="attrs"
              :input-value="selected"
              close
              @click="select"
              @click:close="remove(item)"
            >
              <strong>{{ item }}</strong
              >&nbsp;
              <span>(interest)</span>
            </v-chip>
          </template>
        </v-combobox>

        <v-row class="mt-5">
          <input
            type="text"
            onkeypress="return event.charCode >= 48 && event.charCode <= 57"
          />
        </v-row>
        <v-row>
          <v-btn
            @click="(value1 = false), (value2 = true)"
            block
            class="btn"
            outlined
            text
            color="black"
          >
            Next
          </v-btn>
        </v-row>
      </v-form>
    </v-row>
  </v-content>
</template>

<script>
export default {
  auth: false,

  data() {
    return {
      value1: true,
      value2: false,
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    remove(item) {
      this.chips.splice(this.chips.indexOf(item), 1);
      this.chips = [...this.chips];
    },
  },
};
</script> 