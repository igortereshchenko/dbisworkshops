import React from 'react';

import {
    FormInputForDataContainer,
    FormInputForDataLabel,
    GroupContainer
} from './form-input-for-data.styles';

const FormInputForData = ({handleChange, label, ...props}) => (
    <GroupContainer>
        <FormInputForDataContainer onChange={handleChange} {...props} />
        {label ? (
            <FormInputForDataLabel className={props.value.length ? 'shrink' : ''}>
                {label}
            </FormInputForDataLabel>
        ) : null}
    </GroupContainer>
);

export default FormInputForData;