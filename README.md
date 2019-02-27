# Purple-Martin-Bird-Detection
A neural network to detect the birds and find their nest attentiveness.

GOAL:

 Design a video processing model that reduces the time taken to process each video. We are left with 4 TB of video to be processed.

 Train a neural network to detect the birds in each frame (also to find if it’s a female or male or none)

 Find the nest attentiveness of the birds by processing each video.

 Plot the nest attentiveness against the time to find out important details in the nesting birds life.

 Superimpose multiple nest data and find the similarities between different channels.

METHODOLOGY:

 Video processing model processes a frame every second. Frame size is also reduced before processing to save time.

 A 3 layered CNN is used to detect the birds in each frame.

 Nest attentiveness is calculated by this formula.

            NA = (Number of frames with birds present)/(𝑇𝑜𝑡𝑎𝑙 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑓𝑟𝑎𝑚𝑒𝑠 𝐵𝑒𝑖𝑛𝑔 𝑝𝑟𝑜𝑐𝑒𝑠𝑠𝑒𝑑)
            
 Plot Nest attentiveness vs time. Plot different graphs over each other to find the transition between incubation and provisioning.

CHALLENGES

Poor lighting in the videos caused the model to predict a bird even though there was no bird. This issue was resolved by training the model with poorly lighted images also. There was difficulty in distinguishing between male and female birds and distinguishing between a nestling and a parent. Male birds are can be distinguished by their prominent purple colored plumage, but sometimes even young female birds can have purple plumage. This results low accuracy in distinguishing male and female birds (~60%).
