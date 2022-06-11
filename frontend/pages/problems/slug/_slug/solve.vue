<template>
  <v-layout wrap fill-height>
    <v-flex sm6>
      <v-tabs color="deep-purple accent-4" centered>
        <v-tab>Problem Statement</v-tab>
        <v-tab>Previous Submission</v-tab>
        <v-tab>Solutions</v-tab>

        <v-tab-item v-for="n in 3" :key="n">
          <v-container fluid>
            <v-row :key="i">
              <h1>Hello, this is just me testing</h1>
            </v-row>
          </v-container>
        </v-tab-item>
      </v-tabs>
    </v-flex>
    <v-flex sm6>
      <v-card class="mx-auto overflow-hidden rounded-0" height="100%">
        <div class="primary">
          <v-select
            style="width: 25%"
            :items="['Python', 'Java', 'Go', 'Clojure']"
            placeholder="Languages"
            dense
            hide-details="true"
            outlined
            background-color="white"
            class="py-2 pl-2"
          ></v-select>
        </div>

        <codemirror
          ref="myCm"
          :value="code"
          :options="cmOptions"
          @ready="onCmReady"
          @focus="onCmFocus"
          @input="onCmCodeChange"
        >
        </codemirror>
        <div>
          <v-btn class="ma-1" color="green" dense> Run </v-btn>
          <v-btn class="ma-1" color="primary black--text" dense> Submit </v-btn>
        </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
// theme css
import "codemirror/theme/dracula.css";
// more codemirror resources
import "codemirror/mode/sql/sql.js";
import "codemirror/mode/python/python.js";
import "codemirror/mode/go/go.js";
import "codemirror/mode/haskell/haskell.js";
import "codemirror/mode/clojure/clojure.js";

// import 'codemirror/some-resource...'
export default {
  data() {
    return {
      code: "const a = 10",
      cmOptions: {
        // codemirror options
        tabSize: 4,
        mode: { name: "sql" },
        theme: "dracula",
        lineNumbers: true,
        line: true,
      },
    };
  },
  methods: {
    onCmReady(cm) {
      console.log("the editor is readied!", cm);
    },
    onCmFocus(cm) {
      console.log("the editor is focus!", cm);
    },
    onCmCodeChange(newCode) {
      console.log("this is new code", newCode);
      this.code = newCode;
    },
  },
  computed: {
    codemirror() {
      return this.$refs.myCm.codemirror;
    },
  },
  mounted() {
    // console.log("this is current codemirror object", this.codemirror);
    // you can use this.codemirror to do something...
  },
};
</script>