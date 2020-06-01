import {createSelector} from "reselect";

const selectSidebar = state => state.sidebar;

export const selectSidebarHidden = createSelector(
    [selectSidebar],
    sidebar => sidebar.hidden
);