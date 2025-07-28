# scripts/training/auto_fine_tuner.py
from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments, Trainer

from backend.altiora.core.feedback.feedback_collector import FeedbackCollector

TRIGGER_THRESHOLD = 50  # votes ≥ 3


async def should_trigger():
    collector = FeedbackCollector()
    batch = await collector.get_batch()
    return len(batch) >= TRIGGER_THRESHOLD


async def schedule_retrain():
    dataset = await build_dataset_from_feedback()

    lora_config = LoraConfig(
        r=32,
        lora_alpha=64,  # 2×r (meilleur loss) [^10^]
        lora_dropout=0.1,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        task_type="CAUSAL_LM"
    )

    training_args = TrainingArguments(
        output_dir="./models/lora_adapters",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        fp16=True,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_steps=10,
        report_to="mlflow"
    )

    trainer = Trainer(
        model=get_peft_model(base_model, lora_config),
        args=training_args,
        train_dataset=dataset,
        eval_dataset=dataset.select(range(50))
    )

    trainer.train()
    trainer.save_model("./models/lora_adapters/latest")