package pamiw.eepw.notesapp.dto;

import com.fasterxml.jackson.annotation.JsonView;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Builder;
import lombok.Value;
import lombok.extern.jackson.Jacksonized;

@Value
@Builder
@Jacksonized
public class NoteDto {

    @Schema(description = "Note primary key")
    @JsonView({Views.Get.class, Views.Put.class})
    Long id;

    @Schema(description = "Note title", example = "My note")
    @JsonView({Views.Get.class, Views.Put.class, Views.Post.class})
    String title;

    @Schema(description = "Note text", example = "Some text")
    @JsonView({Views.Get.class, Views.Put.class, Views.Post.class})
    String content;
}
