# robotic-folding
An implementation of A Geometric Approach to Laundry Folding done in ROS and python. More information can be found at http://rll.berkeley.edu/IJRR2011/

# Folding Robot
* Five main stacks
* for pkg in berkeley_demos berkeley_utils folding pr2_simple_motions visual_feedback; 
do svn co svn+ssh://svn@rll.berkeley.edu/main/berkeley-ros-pkg/stacks/$pkg/tags/willow/$pkg; 
done

## `pr2_simple_motions`
### Packages
#### `pr2_simple_arm_motions`
* **Brief** : Provides a framework for moving the arms. Particularly meant for manipulating nonrigid objects.

|Scripts/Node|Description|
|--|--|
|`move_gripper.py` |services for moving the gripper |
|`grip_watcher.py`| "Watches" the gripper to determine whether or not it is holding cloth. Does not require touch sensors. |
|`gripper_tip_frame.py`|Broadcasts a "tip" frame which we find more useful than the tool frame for our tasks.|
|`table_frame.py`|Broadcasts a frame for the table, assuming we are operating on one. _Requires a global parameter "table_height" to be set_|


|Src/Include Files|Description|
|--|--|
|`GripUtils.py`|Simple functions for moving the arm, grabbing objects, etc. Used very frequently in our code|
|`ArmMotionStates.py`| Some common arm-related Smach states.|


|Launch File|Description|
|--|--|
|`move_arms.launch`|Launches the arm controllers + move_gripper services|

#### `pr2_simple_[head/torso/base]_motions`
 * ***Brief***: Same idea as before for various other parts of the robot. Less interesting and probably self-explanatory.
 
#### `pr2_arm_move_ik_synced`
* ***Brief***: Modeled directly after pr2_arm_move_ik, but adds synchronization so one arm doesn't outrun the other.
* Source Files: See original pr2_arm_move_ik
#### `    pr2_simple_motions_[msgs/srvs]`
* ***Brief***: Hosts the messages and services we use to move the robot. Again, should be self explanatory.

#### `    pr2_simple_motions_apps`
* **Brief**: Combines the packages to allow us to move the whole robot. The particular contribution, aside from basic launch files, is the addition of Stance and Primitive servers, which let us save the instantaneous position of the robot's arms/head/torso/base in Cartesian space rather than joint space, and recall them later.

|Scripts/Nodes|Description|
|--|--|
|`stance_server.py`|Initiates a server which can save the instantaneous pose of the robot to disk and provide services to call to move to said pose|
|`primitive_server.py`|Initiates a server which can save timed sequences of multiple stances to disk and provide services to call to execute said sequence|
|`location_server.py`|Initiates a server which can save locations in the map frame and provide services to go to said location|
_Not sure about the rest: I've never seen them used, and will delete unless an undergrad claims it_

|Launch Files|Description|
|--|--|
|`move_all.launch`|        Initiates control of the entire PR2|
|`stances_and_primitives.launch`|  Example launch file for stance & primitive servers(see berkeley_demos/*/launch/stances.launch for more examples)|

## `folding`
* **Brief**: Contains all packages relevant to executing folds in fabric
### Packages
#### `folding_geometry`
* **Brief**: Handles the 2D geometry of folding, as well as how to convert from 3D cloth points to this representation

|Scripts/Nodes|Description|
|--|--|
|`generate_poly_from_points.py`| Takes in a stream of 3D points, outputs a "polygon". Relavent when there is no assumption for flat table |
 |`poly_gui_bridge.py`|Takes a 3D polygon as input, and interfaces with the FoldingGUI window to display the polygon and track folds/etc in it. Also publishes output fold trajectories for others nodes (such as the fold_executor) to use.|

|Src/Include Files|Descriptions|
|--|--|
|`FoldingGUI.py`|Extends the ShapeWindow.py framework to allow us to draw and fold arbitrary polygons. Also contains primitive fold sequences for shirts, sweaters, pants, and towels.|

#### `folding_execution`
* **Brief**: Making the robot actually fold

|Scripts/Nodes|Description|
|--|--|
|`fold_executor.py`|Takes a 3D fold specification as input and executes the folding maneuver with the PR2|

#### ` folding_vision`
* **Brief**: Provides vision to the fold procedure (added later, hence the strange modularity)

|Scripts/Nodes|Description|
|--|--|
|`vision_bridge.py`|Interfaces with our vision systems to update the 2D representation of the cloth polygon we are folding, while we fold it.|

| Launch Files| Description|
|--|--|
|`vision.launch`|Launches the necessary vision nodes for the folding task|

#### `folding_apps`
* **Brief** : Meant to join all folding together. At the moment it only consists of launch files.

| Launch Files| Description|
|--|--|
|`gui_interface.launch`|Launches the interface. Will require you to call: `vision_bridge_node/locate_polygon` to start the `detection/folding` process

## `visual_feedback`
* **Brief**: Where all the actual computer vision is done.
### Packages
#### `image_processor`
* **Brief**: The core package for us to run a vision system on the robot. Provides, in effect, a wrapper which handles any 3D information (stereo or intersection with a known table) and data output. All that is required of us is to fill in one function: process, which takes a 2D image as input and outputs points, parameters, and an optional annotated image.

|Scripts/Nodes|Description|
|--|--|
|`image_processor_node`|The basic node which all others inherit from|
|`click_node.py`|A good human-in-the-loop "vision" system for debugging: when presented with a camera image, pops up with a window for us to click on points on the image manually.|
|`clump_center_node.py`|Returns the center of an object on a green background|
|`furthest_corner_node.py`|Returns the furthest corner (left or right) of the article of cloth on the table|
|`shape_fitter_node.py`|Fits a shape model (see Miller ICRA2011) to the object in the image. Outputs a set of landmark points for the robot to work with.|
|`triangle_fitter_node.py`|A special case of the shape model which uses additional appearance information to determine which half of the towel is the front and back when it is held by two opposite corners.|

#### `visual_feedback_utils`
* **Brief**:Contains utility functions for a lot of shared vision tasks.

| Scripts/Nodes|Description|
|--|--|
|`annotator.py`| Used to annotate points on images and provide ground truth to compare results to|

|Src/Include Files|Description|
|--|--|
|`shape_fitting.py`|Contains code for fitting shape models to contours|
|`thresholding.py`|Threshold out green or white backgrounds, and trace the contour|
|`Vector2D.py`|Basic 2D geometry package with some easy tools for what we're doing|
|`pickle_utils.py`|Used for saving our models to disc|
|`TopicUtils.py`|Provides methods for pulling a single message from a topic, as we need to do image processing when the camera is in streaming mode

#### `clothing_models`
* **Brief**: Provides the models we use for shape fitting, and an example of how to run them on image files

|Scripts/Nodes|Description|
|--|--|
|`birdseye_maker.py`|Converts images to the birdseye view (should be in utils)|
|`comparer.py`|Used for comparing predicted and gruond-truth points|
|`model_maker.py`|Used to design new clothing shape models|
|`fold_maker.py`|Used to generate new models from existing ones by adding a fold line|
|`fit_cloth_models.py`|Example of how to run the fitting procedure|

## `berkeley_utils`
* **Brief**: Misc packages we've developed that didn't necessarily fit under another stack.
### Packages
#### `stereo_click`
* **Brief**: Lets us click on points in an updating camera feed, and streams 3D points out.

|Scripts/Nodes| Descriptions|
|--|--|
|`click_window.py`| The GUI we use for clicking|
|`mono_converter.py`|Determines 3D from a single image assuming intersection with a known plane in the world frame (i.e. a table)|
|`stereo_converter.py`|Determines 3D from two images where corresponding points are clicked.|
|`optical_converter.py`|Determines 3D from time-delayed images (taken from different views)|

|Launch Files|Descriptions|
|--|--|
|`wide_[mono/stereo/optical]_click.launch`| An example of how to use these tools|

#### `shape_window`
* **Brief**: A GUI interface for dealing with shapes, buttons, etc. Used by folding_geometry.FoldingGUI

|`Src/Include Files`|Descriptions|
|--|--|
|`Geometry2D.py`|Package for 2D shapes/geometry. Used extensively by the folding_geometry package|
|`ShapeWindow.py`|Introduces the ShapeWindow class.|

#### `rll_utils`
* **Brief**: Utility functions for dealing with certain, frequently repeated bits of code

|Src/Include Files| Description|
|--|--|
|`RosUtils`|Provides functions for dealing with Services and Topics|
|`TFUtils`|Functions which make it easier to convert between frames assuming we always want now() + error handling|
|`ImageUtils`|Wrappers for img_msg -> cv_image conversions|

#### smach_utils
* **Brief**: Some extensions to Smach state machines, mostly allowing for easy nesting

## berkeley_demos
* **Brief**: Where we throw end-to-end demos we are working on. At this point, it's easiest to ignore all but one:
 
### Packages
#### `unfolding_smach`
* **Brief**: The robot takes a towel from an arbitrary configuration, and folds it
* **Demo Setup**: Assumes we have a table with a green cloth on it, and some sort of padding which lets the robot get under the clothing easily. The table must be narrow enough for the robot's arms to be able to reach across from oneend to the other (left <-> right). 
* A towel begins on the table in an arbitrary pile. The robot will pick it up, drag it across the table, grab the lowest hanging point, and repeat a few times. It will then shake it, and have it in a two-triangle configuration, where one triangle is face up and the other is face down. It shakes it, lays it out, and observes it. It grabs what it observed to be the top half, spreads it out as a rectangle. It then picks it up and flips it, to smooth corners it couldn't fix before. Then it folds it on half, followed by thirds.

* **Scripts/Nodes**: For our purposes, only one: demo.py. This simply needs to be run.
* **Launch files**: There are a few, all of which are combined in `full_demo.launch`. Ideally, you can launch `full_demo.launch`, run demo.py, and need nothing else.
