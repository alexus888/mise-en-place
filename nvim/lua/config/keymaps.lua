-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- open my custom keymap yaml
vim.keymap.set("n", "<leader>fk", function()
  vim.cmd("edit ~/.config/nvim/KEYMAP.txt")
  vim.cmd("wincmd p")
end, { desc = "Open personal keymaps reference" })
