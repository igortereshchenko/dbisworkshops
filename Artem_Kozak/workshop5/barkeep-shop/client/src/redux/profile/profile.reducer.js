import ProfileActionTypes from "./profile.types";

const INITIAL_STATE = {
    hidden: true,
};

const profileReducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case ProfileActionTypes.PROFILE_UPDATE_HIDDEN:
            return {
                ...state,
                hidden: !state.hidden
            };
        default:
            return state;
    }
};

export default profileReducer;