# coding=utf8
from word_breaker.word_segment_v5 import WordSegment

# text = "အဘယ်ကြောင့် ဆိုသော် ထိုသူငယ်မသည် မတော်တဆ ကံအားလျော်စွာ ရရှိထားသော တန်ခိုးသတ္တိထူးကို သူငယ်တို့ ဘာဝ အမှတ်မဲ့အသုံးချခြင်းအားဖြင့် လိုအပ်သောအရာကို ရနိုင်ခဲ့လျှင် နေရာကျအောင် ပိုင်ပိုင်နိုင်နိုင် အသုံးချတတ်သော သင်လူကြီးတယောက်သည် သင်လိုသော ငွေကို လည်းကောင်း၊ သင်လိုသော ကြီးပွားမှုကိုလည်းကောင်း အဘယ်ကြောင့် မရနိုင်ရှိ အံ့နည်း"
text = "သဘာဝဟာသဘာဝပါ"
wordSegmenter = WordSegment()
# Segment using sub_word_possibility segmentation method on Unicode String
print(wordSegmenter.normalize_break(text, 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility))

# Segment using sub_word_possibility segmentation method on Zawgyi String
# print(wordSegmenter.normalize_break('၎င်း နည်းလမ်းများသည်', 'zawgyi', wordSegmenter.SegmentationMethod.sub_word_possibility))

# # Segment using all_possible_combination segmentation method on Unicode String
# print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'unicode', wordSegmenter.SegmentationMethod.all_possible_combination))

# # Segment using all_possible_combination segmentation method on Zawgyi String
# print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'zawgyi', wordSegmenter.SegmentationMethod.all_possible_combination))