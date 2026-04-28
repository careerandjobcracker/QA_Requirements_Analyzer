import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        widget1: resolve(__dirname, 'widget1-core-analyzer.html'),
        widget2: resolve(__dirname, 'widget2-advanced-analysis.html'),
        widget3: resolve(__dirname, 'widget3-generation-operations.html'),
        widget4: resolve(__dirname, 'widget4-workspace.html'),
        widget5: resolve(__dirname, 'widget5-ai-tools.html'),
      },
    },
  },
})
