import React from 'react';
import Button from './Button';


export default {
    title: 'Application/Component Library/Button',
    component: Button,
    controls: {
        hideNoControlsWarning: true
    }
}

// We create a "template" of how args map to rendering
const Template = (args) => <Button {...args} />;

// Each story then reuses that template
export const Default = Template.bind({});
Default.parameters = {
    controls: { hideNoControlsWarning: true }
}
Default.args = {
    children: 'Click Me'
}
