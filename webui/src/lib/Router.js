export const router = {
  navigate: (path) => {
    window.history.pushState({}, "", path);
    window.dispatchEvent(new Event("popstate"));
  },
};
