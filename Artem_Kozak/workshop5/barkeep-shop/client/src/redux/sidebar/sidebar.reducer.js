import SidebarActionTypes from "./sidebar.types";

const INITIAL_STATE = {
    hidden: true,
};

const sidebarReducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case SidebarActionTypes.SIDEBAR_HIDDEN:
            return {
                ...state,
                hidden: !state.hidden
            };
        default:
            return state;
    }
};

export default sidebarReducer;